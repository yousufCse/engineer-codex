# PART 9: Flutter ও Mobile Networking
## Flutter Developer-এর নেটওয়ার্কিং Masterclass

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩০: Flutter-এ HTTP/REST — সঠিকভাবে করার উপায়

## ৩০.১ Flutter-এ HTTP Stack

```
Flutter HTTP Request যাত্রা:

Dart Code (Dio/http)
        │
        ▼
Dart dart:io (HttpClient)
        │
        ▼
Platform Channel (Android/iOS)
        │
        ▼
OS Network Stack
(Android: OkHttp under the hood)
(iOS: URLSession under the hood)
        │
        ▼
Network Interface (Wi-Fi/4G)
        │
        ▼
Internet → Server
```

## ৩০.২ http Package vs Dio — কোনটি কখন?

```
http Package:
✓ Simple, lightweight
✓ Official Dart team maintain করে
✓ Small apps-এ ভালো
✗ Interceptor নেই
✗ Cancel করা কঠিন
✗ Auto retry নেই
✗ Progress tracking নেই

Dio Package:
✓ Interceptors (Auth, Logging, Retry)
✓ Request Cancellation
✓ Progress Callback
✓ FormData / Multipart
✓ Auto Retry
✓ Certificate Pinning
✓ Transformer (custom serialization)
✗ Heavier dependency

সিদ্ধান্ত:
Simple app / Prototype → http
Production Flutter app → Dio
```

## ৩০.৩ Production-Ready Dio Setup

```dart
import 'package:dio/dio.dart';
import 'package:pretty_dio_logger/pretty_dio_logger.dart';

class DioClient {
  static Dio? _instance;
  
  static Dio get instance {
    _instance ??= _createDio();
    return _instance!;
  }
  
  static Dio _createDio() {
    final dio = Dio(
      BaseOptions(
        baseUrl: AppConfig.apiBaseUrl,
        connectTimeout: const Duration(seconds: 10),
        receiveTimeout: const Duration(seconds: 30),
        sendTimeout: const Duration(seconds: 30),
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'Accept': 'application/json',
          'Accept-Language': 'bn, en',
          'X-App-Version': AppConfig.version,
          'X-Platform': Platform.operatingSystem,
        },
        responseType: ResponseType.json,
        validateStatus: (status) => status != null && status < 500,
      ),
    );
    
    // Interceptors যোগ করি (ক্রম গুরুত্বপূর্ণ!)
    dio.interceptors.addAll([
      _AuthInterceptor(),    // ১ম — Token যোগ করে
      _RetryInterceptor(),   // ২য় — Retry handle করে
      _ErrorInterceptor(),   // ৩য় — Error normalize করে
      if (kDebugMode)
        PrettyDioLogger(    // ৪র্থ — Debug logging
          requestBody: true,
          responseBody: true,
          maxWidth: 90,
        ),
    ]);
    
    return dio;
  }
}

// Auth Interceptor — JWT Token
class _AuthInterceptor extends Interceptor {
  @override
  void onRequest(
    RequestOptions options,
    RequestInterceptorHandler handler,
  ) async {
    final token = await AuthService.instance.getValidToken();
    if (token != null) {
      options.headers['Authorization'] = 'Bearer $token';
    }
    handler.next(options);
  }
  
  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    if (err.response?.statusCode == 401) {
      // Token expire → refresh করি
      final refreshed = await AuthService.instance.refreshToken();
      if (refreshed) {
        // Original request আবার করি
        final opts = err.requestOptions;
        final newToken = await AuthService.instance.getValidToken();
        opts.headers['Authorization'] = 'Bearer $newToken';
        try {
          final response = await DioClient.instance.fetch(opts);
          handler.resolve(response);
          return;
        } catch (e) {
          // Refresh failed
        }
      }
      // Refresh failed → logout
      AuthService.instance.logout();
    }
    handler.next(err);
  }
}

// Retry Interceptor — Exponential Backoff
class _RetryInterceptor extends Interceptor {
  static const int _maxRetries = 3;
  
  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    final retryCount = err.requestOptions.extra['retryCount'] ?? 0;
    
    final shouldRetry = _shouldRetry(err) && retryCount < _maxRetries;
    
    if (shouldRetry) {
      // Exponential backoff: 1s, 2s, 4s
      final delay = Duration(seconds: 1 << retryCount);
      await Future.delayed(delay);
      
      err.requestOptions.extra['retryCount'] = retryCount + 1;
      try {
        final response = await DioClient.instance.fetch(err.requestOptions);
        handler.resolve(response);
        return;
      } catch (e) {
        // Continue to error handling
      }
    }
    
    handler.next(err);
  }
  
  bool _shouldRetry(DioException err) {
    return err.type == DioExceptionType.connectionTimeout ||
        err.type == DioExceptionType.receiveTimeout ||
        err.type == DioExceptionType.connectionError ||
        (err.response?.statusCode ?? 0) >= 500;
  }
}

// Error Interceptor — Normalize errors
class _ErrorInterceptor extends Interceptor {
  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    final apiError = ApiError.fromDioException(err);
    handler.next(
      err.copyWith(error: apiError),
    );
  }
}
```

## ৩০.৪ Request Cancellation

```dart
// Request Cancel করার উপায়:
class SearchRepository {
  CancelToken? _searchCancelToken;
  
  Future<List<Product>> search(String query) async {
    // আগের search cancel করি
    _searchCancelToken?.cancel('New search started');
    _searchCancelToken = CancelToken();
    
    try {
      final response = await DioClient.instance.get(
        '/products/search',
        queryParameters: {'q': query},
        cancelToken: _searchCancelToken,
      );
      return (response.data as List)
          .map((e) => Product.fromJson(e))
          .toList();
    } on DioException catch (e) {
      if (CancelToken.isCancel(e)) {
        return []; // Cancelled — no error
      }
      rethrow;
    }
  }
  
  void dispose() {
    _searchCancelToken?.cancel();
  }
}

// Flutter Widget-এ:
class SearchWidget extends StatefulWidget {
  @override
  State<SearchWidget> createState() => _SearchWidgetState();
}

class _SearchWidgetState extends State<SearchWidget> {
  final _repo = SearchRepository();
  
  @override
  void dispose() {
    _repo.dispose(); // widget dispose-এ cancel
    super.dispose();
  }
}
```

## ৩০.৫ File Upload with Progress

```dart
Future<String> uploadFile(File file) async {
  final fileName = path.basename(file.path);
  final mimeType = lookupMimeType(file.path) ?? 'application/octet-stream';
  
  final formData = FormData.fromMap({
    'file': await MultipartFile.fromFile(
      file.path,
      filename: fileName,
      contentType: MediaType.parse(mimeType),
    ),
    'description': 'Profile photo',
  });
  
  final response = await DioClient.instance.post(
    '/upload',
    data: formData,
    onSendProgress: (sent, total) {
      final progress = sent / total;
      // UI update: UploadProgressNotifier.update(progress)
      print('Upload: ${(progress * 100).toStringAsFixed(1)}%');
    },
    options: Options(
      receiveTimeout: const Duration(minutes: 5), // Large file
    ),
  );
  
  return response.data['url'] as String;
}

// Download with Progress:
Future<void> downloadFile(String url, String savePath) async {
  await DioClient.instance.download(
    url,
    savePath,
    onReceiveProgress: (received, total) {
      if (total != -1) {
        final progress = received / total;
        print('Download: ${(progress * 100).toStringAsFixed(1)}%');
      }
    },
    cancelToken: _cancelToken,
  );
}
```

## ৩০.৬ Response Caching

```dart
import 'package:dio_cache_interceptor/dio_cache_interceptor.dart';

// Cache Setup:
final cacheOptions = CacheOptions(
  store: HiveCacheStore('cache_dir'), // Hive-based persistent cache
  policy: CachePolicy.request,        // Network first, cache fallback
  hitCacheOnErrorExcept: [401, 403], // Error হলেও cache দেখাও
  maxStale: const Stale(days: 7),    // Cache 7 দিন পর্যন্ত valid
  priority: CachePriority.normal,
);

dio.interceptors.add(DioCacheInterceptor(options: cacheOptions));

// Per-request cache control:
final response = await dio.get(
  '/products',
  options: cacheOptions.copyWith(
    policy: CachePolicy.forceCache, // সবসময় cache ব্যবহার (offline)
  ).toOptions(),
);

// Cache invalidate করা:
await cacheOptions.store!.clean(
  priority: CachePriority.normal, // normal priority-র cache মুছি
);

// Conditional Request (ETag):
// সার্ভার থেকে ETag পাই:
// ETag: "abc123"
// পরের request-এ পাঠাই:
// If-None-Match: "abc123"
// পরিবর্তন না হলে: 304 Not Modified (body নেই, bandwidth save!)
```

## ৩০.৭ Network-Aware UI

```dart
import 'package:connectivity_plus/connectivity_plus.dart';

class NetworkStatusNotifier extends ChangeNotifier {
  ConnectivityResult _status = ConnectivityResult.none;
  
  ConnectivityResult get status => _status;
  bool get isOnline => _status != ConnectivityResult.none;
  
  NetworkStatusNotifier() {
    _init();
  }
  
  void _init() {
    Connectivity().onConnectivityChanged.listen((result) {
      _status = result;
      notifyListeners();
    });
  }
}

// Widget:
class NetworkAwareWidget extends StatelessWidget {
  final Widget child;
  const NetworkAwareWidget({required this.child});
  
  @override
  Widget build(BuildContext context) {
    return Consumer<NetworkStatusNotifier>(
      builder: (context, network, _) {
        return Stack(
          children: [
            child,
            if (!network.isOnline)
              Positioned(
                bottom: 0, left: 0, right: 0,
                child: Container(
                  color: Colors.red,
                  padding: const EdgeInsets.all(8),
                  child: const Text(
                    '📵 ইন্টারনেট সংযোগ নেই',
                    textAlign: TextAlign.center,
                    style: TextStyle(color: Colors.white),
                  ),
                ),
              ),
          ],
        );
      },
    );
  }
}
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩১: Flutter-এ WebSocket ও Real-time

## ৩১.১ WebSocket vs Push Notification

```
Push Notification:
┌───────────────────────────────────────────────┐
│ App Background/Closed হলেও কাজ করে           │
│ OS handle করে (FCM, APNs)                     │
│ Battery efficient                              │
│ Server → Client শুধু                          │
│ Use: New message alert, order update          │
└───────────────────────────────────────────────┘

WebSocket:
┌───────────────────────────────────────────────┐
│ App Foreground-এ থাকতে হয়                    │
│ App handle করে                                │
│ Battery বেশি খরচ                              │
│ Client ↔ Server দুমুখী                        │
│ Use: Live chat, Real-time collaboration       │
└───────────────────────────────────────────────┘

Best Practice:
App Open → WebSocket চালু (real-time)
App Close → WebSocket বন্ধ, Push Notification নির্ভর
```

## ৩১.২ Production-Ready WebSocket Service

```dart
import 'dart:async';
import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:web_socket_channel/status.dart' as status;

enum WebSocketState { disconnected, connecting, connected, reconnecting }

class RealtimeService {
  static final RealtimeService instance = RealtimeService._();
  RealtimeService._();
  
  WebSocketChannel? _channel;
  Timer? _heartbeatTimer;
  Timer? _reconnectTimer;
  
  int _reconnectAttempts = 0;
  static const int _maxReconnectAttempts = 10;
  static const Duration _heartbeatInterval = Duration(seconds: 25);
  
  final _stateController = StreamController<WebSocketState>.broadcast();
  final _messageController = StreamController<Map<String, dynamic>>.broadcast();
  
  Stream<WebSocketState> get stateStream => _stateController.stream;
  Stream<Map<String, dynamic>> get messageStream => _messageController.stream;
  
  WebSocketState _state = WebSocketState.disconnected;
  
  // Connect
  Future<void> connect() async {
    if (_state == WebSocketState.connecting ||
        _state == WebSocketState.connected) return;
    
    _setState(WebSocketState.connecting);
    
    final token = await AuthService.instance.getValidToken();
    final uri = Uri.parse(
      '${AppConfig.wsBaseUrl}/ws?token=$token'
    );
    
    try {
      _channel = WebSocketChannel.connect(uri);
      await _channel!.ready; // Wait for handshake
      
      _setState(WebSocketState.connected);
      _reconnectAttempts = 0;
      _startHeartbeat();
      
      _channel!.stream.listen(
        _handleMessage,
        onError: _handleError,
        onDone: _handleDisconnect,
        cancelOnError: false,
      );
    } catch (e) {
      _setState(WebSocketState.disconnected);
      _scheduleReconnect();
    }
  }
  
  void _handleMessage(dynamic data) {
    if (data is! String) return;
    
    try {
      final json = jsonDecode(data) as Map<String, dynamic>;
      
      if (json['type'] == 'pong') {
        // Heartbeat response — connection alive
        return;
      }
      
      _messageController.add(json);
    } catch (e) {
      print('Invalid message: $data');
    }
  }
  
  void _handleError(dynamic error) {
    print('WebSocket error: $error');
    _cleanup();
    _scheduleReconnect();
  }
  
  void _handleDisconnect() {
    _setState(WebSocketState.disconnected);
    _cleanup();
    _scheduleReconnect();
  }
  
  void _startHeartbeat() {
    _heartbeatTimer?.cancel();
    _heartbeatTimer = Timer.periodic(_heartbeatInterval, (_) {
      send({'type': 'ping', 'ts': DateTime.now().millisecondsSinceEpoch});
    });
  }
  
  // Exponential Backoff Reconnect
  void _scheduleReconnect() {
    if (_reconnectAttempts >= _maxReconnectAttempts) {
      print('Max reconnect attempts. Giving up.');
      return;
    }
    
    _setState(WebSocketState.reconnecting);
    
    // With jitter: avoid thundering herd
    final baseDelay = 1 << _reconnectAttempts.clamp(0, 6); // max 64s
    final jitter = (baseDelay * 0.2).round();
    final delay = Duration(
      seconds: baseDelay + (Random().nextInt(jitter) - jitter ~/ 2),
    );
    
    _reconnectAttempts++;
    print('Reconnecting in ${delay.inSeconds}s (attempt $_reconnectAttempts)');
    
    _reconnectTimer?.cancel();
    _reconnectTimer = Timer(delay, connect);
  }
  
  // Message পাঠানো
  void send(Map<String, dynamic> data) {
    if (_state != WebSocketState.connected) return;
    _channel?.sink.add(jsonEncode(data));
  }
  
  void _cleanup() {
    _heartbeatTimer?.cancel();
  }
  
  void _setState(WebSocketState newState) {
    _state = newState;
    _stateController.add(newState);
  }
  
  // Disconnect
  Future<void> disconnect() async {
    _reconnectTimer?.cancel();
    _heartbeatTimer?.cancel();
    await _channel?.sink.close(status.goingAway);
    _channel = null;
    _setState(WebSocketState.disconnected);
  }
  
  // Dispose
  void dispose() {
    disconnect();
    _stateController.close();
    _messageController.close();
  }
}

// Flutter Widget-এ ব্যবহার:
class ChatScreen extends StatefulWidget {
  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen>
    with WidgetsBindingObserver {
  
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    RealtimeService.instance.connect();
  }
  
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    switch (state) {
      case AppLifecycleState.resumed:
        RealtimeService.instance.connect(); // App foreground → reconnect
        break;
      case AppLifecycleState.paused:
        RealtimeService.instance.disconnect(); // App background → disconnect
        break;
      default:
        break;
    }
  }
  
  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }
}
```

## ৩১.৩ Firebase Realtime Database — নেটওয়ার্ক Internals

```
Firebase Realtime Database (বা Firestore) কিভাবে কাজ করে:

Flutter App → Firebase SDK → WebSocket/gRPC → Firebase Servers

Firebase-র Network Behavior:
1. Offline Support:
   - Local cache-এ write হয়
   - Online হলে sync হয়
   
2. Real-time sync:
   - Long-polling বা WebSocket
   - Server-Sent Events

3. Conflict Resolution:
   - Timestamp-based
   - Last Write Wins

Flutter-এ Firebase Realtime:
```

```dart
import 'package:firebase_database/firebase_database.dart';

class ChatRepository {
  final _db = FirebaseDatabase.instance;
  
  // Real-time listen:
  Stream<List<Message>> getMessages(String roomId) {
    return _db
        .ref('chats/$roomId/messages')
        .orderByChild('timestamp')
        .limitToLast(50)
        .onValue
        .map((event) {
          final data = event.snapshot.value as Map?;
          if (data == null) return [];
          
          return data.entries
              .map((e) => Message.fromMap(
                    Map<String, dynamic>.from(e.value as Map),
                  ))
              .toList();
        });
  }
  
  // Offline-capable write:
  Future<void> sendMessage(String roomId, String text) async {
    // Firebase SDK handles offline queue automatically!
    await _db.ref('chats/$roomId/messages').push().set({
      'text': text,
      'userId': AuthService.currentUserId,
      'timestamp': ServerValue.timestamp,
    });
  }
}
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩২: Flutter-এ gRPC ও GraphQL

## ৩২.১ Flutter gRPC Setup

```bash
# pubspec.yaml:
dependencies:
  grpc: ^3.2.4
  protobuf: ^3.1.0

dev_dependencies:
  protoc_plugin: ^21.1.2

# Proto file থেকে code generate:
# Windows:
# protoc --dart_out=grpc:lib/src/generated -I protos protos/*.proto

# Script (Makefile):
# make proto
```

```protobuf
// protos/chat.proto
syntax = "proto3";
package chat;

message Message {
  string id = 1;
  string room_id = 2;
  string user_id = 3;
  string text = 4;
  int64 created_at = 5;
}

message SendMessageRequest {
  string room_id = 1;
  string text = 2;
}

message GetMessagesRequest {
  string room_id = 1;
  int32 page_size = 2;
  string page_token = 3;
}

message GetMessagesResponse {
  repeated Message messages = 1;
  string next_page_token = 2;
}

service ChatService {
  rpc SendMessage (SendMessageRequest) returns (Message);
  rpc GetMessages (GetMessagesRequest) returns (GetMessagesResponse);
  rpc SubscribeToRoom (SubscribeRequest) returns (stream Message);
}
```

```dart
// gRPC Client:
import 'package:grpc/grpc.dart';
import 'generated/chat.pbgrpc.dart';

class ChatGrpcClient {
  late final ClientChannel _channel;
  late final ChatServiceClient _stub;
  
  ChatGrpcClient() {
    _channel = ClientChannel(
      AppConfig.grpcHost,
      port: AppConfig.grpcPort,
      options: const ChannelOptions(
        credentials: ChannelCredentials.secure(),
        connectionTimeout: Duration(seconds: 10),
        idleTimeout: Duration(minutes: 5),
        codecRegistry: CodecRegistry(
          codecs: [GzipCodec(), IdentityCodec()],
        ),
      ),
    );
    
    _stub = ChatServiceClient(
      _channel,
      options: CallOptions(
        timeout: const Duration(seconds: 30),
        metadata: {'x-app-version': AppConfig.version},
      ),
    );
  }
  
  // Unary
  Future<Message> sendMessage(String roomId, String text) async {
    final request = SendMessageRequest()
      ..roomId = roomId
      ..text = text;
    
    final token = await AuthService.instance.getValidToken();
    return await _stub.sendMessage(
      request,
      options: CallOptions(
        metadata: {'authorization': 'Bearer $token'},
      ),
    );
  }
  
  // Server Streaming — Real-time messages
  Stream<Message> subscribeToRoom(String roomId) {
    final request = SubscribeRequest()..roomId = roomId;
    return _stub.subscribeToRoom(request);
  }
  
  Future<void> dispose() async {
    await _channel.shutdown();
  }
}

// Widget-এ streaming:
StreamBuilder<Message>(
  stream: _grpcClient.subscribeToRoom(widget.roomId),
  builder: (context, snapshot) {
    if (snapshot.hasData) {
      // নতুন message এলো!
      _messages.add(snapshot.data!);
    }
    return MessageList(messages: _messages);
  },
)
```

## ৩২.২ Flutter-এ GraphQL

```dart
// pubspec.yaml:
// graphql_flutter: ^5.1.2

import 'package:graphql_flutter/graphql_flutter.dart';

// GraphQL Client Setup:
class GraphQLConfig {
  static GraphQLClient getClient() {
    final httpLink = HttpLink('https://api.myapp.com/graphql');
    
    final authLink = AuthLink(
      getToken: () async {
        final token = await AuthService.instance.getValidToken();
        return 'Bearer $token';
      },
    );
    
    final wsLink = WebSocketLink(
      'wss://api.myapp.com/graphql',
      config: SocketClientConfig(
        autoReconnect: true,
        inactivityTimeout: const Duration(minutes: 5),
        initialPayload: () async {
          final token = await AuthService.instance.getValidToken();
          return {'authorization': 'Bearer $token'};
        },
      ),
    );
    
    // Query/Mutation → HTTP, Subscription → WebSocket
    final link = authLink.concat(
      Link.split(
        (request) => request.isSubscription,
        wsLink,
        httpLink,
      ),
    );
    
    return GraphQLClient(
      link: link,
      cache: GraphQLCache(store: HiveStore()),
    );
  }
}

// Query:
const getProductsQuery = gql(r'''
  query GetProducts($category: String!, $limit: Int!) {
    products(category: $category, limit: $limit) {
      id
      name
      price
      thumbnail
      rating {
        average
        count
      }
    }
  }
''');

// Widget-এ:
Query(
  options: QueryOptions(
    document: getProductsQuery,
    variables: {'category': 'electronics', 'limit': 20},
    fetchPolicy: FetchPolicy.cacheAndNetwork,
  ),
  builder: (result, {refetch, fetchMore}) {
    if (result.hasException) return ErrorWidget(result.exception!);
    if (result.isLoading) return const LoadingWidget();
    
    final products = (result.data!['products'] as List)
        .map((e) => Product.fromJson(e))
        .toList();
    
    return ProductGrid(products: products);
  },
)

// Subscription (Real-time):
const onMessageSubscription = gql(r'''
  subscription OnMessage($roomId: String!) {
    messageAdded(roomId: $roomId) {
      id
      text
      user { id name }
      createdAt
    }
  }
''');

Subscription(
  options: SubscriptionOptions(
    document: onMessageSubscription,
    variables: {'roomId': widget.roomId},
  ),
  builder: (result) {
    if (result.hasData) {
      final message = Message.fromJson(result.data!['messageAdded']);
      // নতুন message এলো!
    }
    return MessageList();
  },
)
```

## ৩২.৩ gRPC vs REST vs GraphQL — Flutter-এ সিদ্ধান্ত

```
Flutter Project Decision Matrix:

┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  প্রশ্ন ১: Backend কি public API?                              │
│  হ্যাঁ → REST (সবচেয়ে ব্যাপকভাবে সমর্থিত)                    │
│                                                                 │
│  প্রশ্ন ২: Complex, nested data দরকার?                         │
│  হ্যাঁ → GraphQL (flexible querying)                           │
│                                                                 │
│  প্রশ্ন ৩: High performance, microservice backend?             │
│  হ্যাঁ → gRPC                                                  │
│                                                                 │
│  প্রশ্ন ৪: Real-time দরকার?                                    │
│  সবাই করতে পারে — WebSocket/gRPC Streaming/GraphQL Subscription│
│                                                                 │
│  প্রশ্ন ৫: Team কি protobuf জানে?                             │
│  না → REST বা GraphQL দিয়ে শুরু করুন                          │
│                                                                 │
│  আমার recommendation for Flutter:                              │
│  ✓ Public/Third-party API → REST (Dio)                         │
│  ✓ Own backend + complex data → GraphQL                        │
│  ✓ Own backend + microservices + performance → gRPC             │
└─────────────────────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩৩: Mobile Network Optimization — ব্যাটারি ও ডেটা সাশ্রয়

## ৩৩.১ Offline-First Architecture

```
Online-First (সমস্যা):
No Internet → App কাজ করে না
User experience খারাপ

Offline-First:
┌──────────────────────────────────────────────────────┐
│                                                      │
│  User Action                                         │
│       │                                              │
│       ▼                                              │
│  Local Database (Hive/SQLite/Isar)                  │
│       │                                              │
│  UI Update তাৎক্ষণিক                                │
│       │                                              │
│  Background Sync (Internet হলে)                     │
│       │                                              │
│  Remote Server                                       │
│                                                      │
└──────────────────────────────────────────────────────┘

User কখনো "Loading..." দেখে না!
```

```dart
// Offline-First Repository Pattern:
class ProductRepository {
  final ProductLocalDataSource _local;   // Hive/SQLite
  final ProductRemoteDataSource _remote; // API
  
  // Read: Local first, then sync
  Stream<List<Product>> getProducts() async* {
    // ১. Local data তাৎক্ষণিক দাও
    final localProducts = await _local.getProducts();
    if (localProducts.isNotEmpty) {
      yield localProducts;
    }
    
    // ২. Background-এ server থেকে নতুন data আনো
    try {
      final remoteProducts = await _remote.getProducts();
      await _local.saveProducts(remoteProducts); // Cache
      yield remoteProducts; // Update UI
    } catch (e) {
      // Network error — local data-ই দেখাও
      if (localProducts.isEmpty) {
        yield []; // Empty state
      }
    }
  }
  
  // Write: Local first, sync later
  Future<void> createOrder(Order order) async {
    // ১. Local-এ save করো (optimistic)
    final localOrder = order.copyWith(
      id: Uuid().v4(),
      syncStatus: SyncStatus.pending,
    );
    await _local.saveOrder(localOrder);
    
    // ২. Background sync
    _syncOrder(localOrder);
  }
  
  Future<void> _syncOrder(Order localOrder) async {
    try {
      final serverOrder = await _remote.createOrder(localOrder);
      await _local.updateOrder(
        localOrder.id,
        serverOrder.copyWith(syncStatus: SyncStatus.synced),
      );
    } catch (e) {
      // Sync failed — পরে আবার try করব
      await _local.updateOrder(
        localOrder.id,
        localOrder.copyWith(syncStatus: SyncStatus.failed),
      );
    }
  }
}
```

## ৩৩.২ Request Batching ও Debouncing

```dart
// Debouncing — Search এর জন্য:
class SearchService {
  Timer? _debounceTimer;
  
  void onSearchChanged(String query) {
    _debounceTimer?.cancel();
    _debounceTimer = Timer(
      const Duration(milliseconds: 500), // 500ms অপেক্ষা
      () => _performSearch(query),
    );
  }
  // User টাইপ করতে থাকলে request যাবে না।
  // থামলে ৫০০ms পর একটি request যাবে।
}

// Request Batching — Multiple requests একসাথে:
class BatchRequestService {
  final List<_PendingRequest> _queue = [];
  Timer? _batchTimer;
  
  Future<User> getUser(String userId) {
    final completer = Completer<User>();
    _queue.add(_PendingRequest(userId, completer));
    
    _batchTimer ??= Timer(
      const Duration(milliseconds: 50), // 50ms-এ batch করি
      _processBatch,
    );
    
    return completer.future;
  }
  
  Future<void> _processBatch() async {
    _batchTimer = null;
    final requests = List<_PendingRequest>.from(_queue);
    _queue.clear();
    
    // এক request-এ সব user আনি:
    final userIds = requests.map((r) => r.userId).toList();
    final users = await _remote.getUsersBatch(userIds);
    
    // প্রতিটি caller-কে তার user দাও:
    for (final request in requests) {
      final user = users.firstWhere((u) => u.id == request.userId);
      request.completer.complete(user);
    }
  }
}
```

## ৩৩.৩ Image Optimization

```dart
// Network Image Best Practices:
class OptimizedImage extends StatelessWidget {
  final String imageUrl;
  final double width;
  final double height;
  
  @override
  Widget build(BuildContext context) {
    final dpr = MediaQuery.of(context).devicePixelRatio;
    final pixelWidth = (width * dpr).round();
    final pixelHeight = (height * dpr).round();
    
    // CDN Image Transformation URL:
    final optimizedUrl = '$imageUrl'
        '?w=$pixelWidth&h=$pixelHeight&q=80&fm=webp&fit=crop';
    
    return CachedNetworkImage(
      imageUrl: optimizedUrl,
      width: width,
      height: height,
      fit: BoxFit.cover,
      // Memory cache: 100MB
      // Disk cache: 1GB, 30 days
      memCacheWidth: pixelWidth,    // Resize in memory
      memCacheHeight: pixelHeight,  // Saves RAM!
      placeholder: (context, url) => const ShimmerBox(),
      errorWidget: (context, url, error) => const FallbackImage(),
    );
  }
}

// Image Preloading:
Future<void> preloadImages(BuildContext context, List<String> urls) async {
  for (final url in urls) {
    await precacheImage(
      CachedNetworkImageProvider(url),
      context,
    );
  }
}
```

## ৩৩.৪ Connection Quality Detection

```dart
class NetworkQualityDetector {
  static Future<NetworkQuality> detect() async {
    final stopwatch = Stopwatch()..start();
    
    try {
      // Small ping request
      final response = await http.get(
        Uri.parse('https://api.myapp.com/ping'),
      ).timeout(const Duration(seconds: 5));
      
      stopwatch.stop();
      final latencyMs = stopwatch.elapsedMilliseconds;
      
      // Latency অনুযায়ী quality:
      if (latencyMs < 100) return NetworkQuality.excellent;
      if (latencyMs < 300) return NetworkQuality.good;
      if (latencyMs < 1000) return NetworkQuality.fair;
      return NetworkQuality.poor;
      
    } catch (e) {
      return NetworkQuality.offline;
    }
  }
}

enum NetworkQuality { excellent, good, fair, poor, offline }

// Adaptive UI:
class AdaptiveVideoPlayer extends StatelessWidget {
  final String videoUrl;
  
  @override
  Widget build(BuildContext context) {
    return FutureBuilder<NetworkQuality>(
      future: NetworkQualityDetector.detect(),
      builder: (context, snapshot) {
        final quality = snapshot.data ?? NetworkQuality.fair;
        
        final resolution = switch (quality) {
          NetworkQuality.excellent => '1080p',
          NetworkQuality.good => '720p',
          NetworkQuality.fair => '480p',
          NetworkQuality.poor => '360p',
          NetworkQuality.offline => null,
        };
        
        if (resolution == null) return const OfflineVideoMessage();
        
        return VideoPlayer(
          url: '$videoUrl?quality=$resolution',
          autoplay: quality != NetworkQuality.fair,
        );
      },
    );
  }
}
```

## ৩৩.৫ Flutter DevTools — Network Profiling

```
Flutter DevTools দিয়ে Network Debug:

1. Flutter DevTools খুলুন:
   flutter run --debug
   # DevTools URL: http://127.0.0.1:9100

2. Network Tab:
   - সব HTTP Request দেখুন
   - Request/Response headers দেখুন
   - Response body দেখুন
   - Timing (DNS, Connect, SSL, Send, Wait, Receive)

3. Performance Tab:
   - Network-related jank খুঁজুন
   - Frame rendering time দেখুন

4. Memory Tab:
   - Image cache size দেখুন
   - Memory leak খুঁজুন

HTTP Inspector দিয়ে:
```

```dart
// Debug mode-এ HTTP traffic দেখা:
if (kDebugMode) {
  dio.interceptors.add(
    PrettyDioLogger(
      requestHeader: true,
      requestBody: true,
      responseBody: true,
      responseHeader: false,
      error: true,
      compact: true,
      maxWidth: 90,
    ),
  );
}

// Charles Proxy / Proxyman দিয়ে HTTPS traffic দেখা:
// iOS Simulator: System Proxy automatically ব্যবহার করে
// Android Emulator: Settings > Proxy ম্যানুয়ালি set করুন
// Real device: Wi-Fi settings-এ proxy set করুন
```

## ৩৩.৬ Battery ও Data Optimization Tips

```
Battery Optimization:
┌─────────────────────────────────────────────────────┐
│ ❌ প্রতি ১ সেকেন্ডে polling                        │
│ ✓ WebSocket + Push Notification (event-driven)     │
│                                                     │
│ ❌ Background-এ WebSocket চালু রাখা                 │
│ ✓ App pause-এ disconnect, resume-এ reconnect        │
│                                                     │
│ ❌ অনেক ছোট request                                │
│ ✓ Request batching                                  │
│                                                     │
│ ❌ বারবার একই data fetch                            │
│ ✓ Cache ব্যবহার করুন                               │
└─────────────────────────────────────────────────────┘

Data Optimization:
┌─────────────────────────────────────────────────────┐
│ ✓ Gzip compression (Accept-Encoding: gzip)         │
│ ✓ JSON minification (কোনো space নেই)               │
│ ✓ Pagination (সব data একসাথে না)                   │
│ ✓ Lazy loading (দরকার হলে load)                    │
│ ✓ WebP format for images (30% smaller than JPEG)   │
│ ✓ Protobuf instead of JSON (60% smaller)           │
│ ✓ HTTP/2 Multiplexing (header compression)         │
│ ✓ Cache-Control headers (bandwidth save)            │
└─────────────────────────────────────────────────────┘
```

**Tech Lead টিপস:**
- Offline-first architecture সব Flutter app-এ implement করুন — ব্যবহারকারী খুশি হয়
- Network profiling regular করুন — অনেক সময় অদৃশ্য data leak থাকে
- Image optimization সবচেয়ে বড় bandwidth saver
- Push Notification + WebSocket hybrid approach সেরা real-time experience

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---
*PART 9 সম্পন্ন। পরবর্তী: PART 10 — System Design ও Architecture*