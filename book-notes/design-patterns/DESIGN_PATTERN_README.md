# Desing Patterns


## (1) Strategy Pattern

*The Strategy Pattern*
    defines a family of algorithms, encapsulates each one,
    and makes them interchangeable.
    Strategy lets the algorithm vary independently from clients that use it.

**Quick Hints**
- *Encapsulate what varies!*
    Put changing algorithms is their own classes.
- *Swap the strategy, change the behavior!*
    Change algorithms at runtime by swapping strategy objets.
- *No more giant if/else or switch!*
    Replace conditional logic with polymorphism.
- *Program to an nterface, not an implementation*
    Use a common interface for all strategies.
- *Favors composition over inheritance!*
    The context HAS-A stragety the need!
- *Clients pick the strategy they need!*
    The context delegates work to the strategy bject.

**Mnemonic**
*I'll use whatever plan(strategy) you give me!*

**Analogy**
*Like a duck that can change how it flies or quacks by swapping out its flying or quacking behvior object.*

- Identify the aspects of your application that vary and seperate them from what staty the same.
- Take what varies and *'encapsulate'* it so it won't affect the rest of your code.
- Separating what changes frm what statys the same.
- Program to an interface, not an implementation.
- Favors composition over inheritance
    - Strategy used composition to change behaviour at runtime,
    rather that inheritance which is static.


**HAS-A can be better than IS-A**
* When you put classe like HAS-A, this is composition. It gives you more flexiblity and can be changed behavior at runtime.
** Favor composition over inheritance.

**UML Class Diagram**
> Real-world example: E-commerce checkout with swappable payment methods

```mermaid
classDiagram
    class ShoppingCart {
        -paymentStrategy: PaymentStrategy
        +setPaymentStrategy(s: PaymentStrategy)
        +checkout(amount: float)
    }
    class PaymentStrategy {
        <<interface>>
        +pay(amount: float)
    }
    class CreditCardPayment {
        -cardNumber: String
        -cvv: String
        +pay(amount: float)
    }
    class PayPalPayment {
        -email: String
        +pay(amount: float)
    }
    class BitcoinPayment {
        -walletAddress: String
        +pay(amount: float)
    }
    ShoppingCart o--> PaymentStrategy
    PaymentStrategy <|.. CreditCardPayment
    PaymentStrategy <|.. PayPalPayment
    PaymentStrategy <|.. BitcoinPayment
```
------------------------------------------------------------------------------


## (2) Factory Method

**Types**
- Factory Method: Subclasses decide what to create.
- Abstract Factory: Create families of related objects.

*The Factory Method Pattern*
    defines an interface for creating an object, but lets subclasses decide
    which class to instantiate.
    Factory Method lets a class defer instantiation to sbclasses.

**Quick Hints**
- *Make, don't take!*
    Don't instantiate object directly- let a factory do it.
- *Encapsulate object creation*
    Hide the new keywords is on place.
- *Let subclasses decide*
    Subclasses of factories choose which class to instantiate.
- *Program to an interface, not an implementation*
    Use interfaces or abstract classes for return types.
- *Factories = Decoupling*
    Client code doesn't need to know concreate classes.
- *If you see lots of new scattered, think Factory!*

**Mnemonic**
*Don't call us, we'll call you (with the right object)!*

**Analogy**
- *Like ordering from a pizza store: you ask for a pizza, the store decides how to make it and hands you the finished product.

**UML Class Diagram**
> Real-world example: Multi-channel notification system (email, SMS, push)

```mermaid
classDiagram
    class NotificationService {
        <<abstract>>
        +createNotification() Notification
        +send(message: String)
    }
    class EmailService {
        +createNotification() Notification
    }
    class SMSService {
        +createNotification() Notification
    }
    class PushService {
        +createNotification() Notification
    }
    class Notification {
        <<interface>>
        +deliver(message: String)
    }
    class EmailNotification {
        -recipient: String
        +deliver(message: String)
    }
    class SMSNotification {
        -phoneNumber: String
        +deliver(message: String)
    }
    class PushNotification {
        -deviceToken: String
        +deliver(message: String)
    }
    NotificationService <|-- EmailService
    NotificationService <|-- SMSService
    NotificationService <|-- PushService
    Notification <|.. EmailNotification
    Notification <|.. SMSNotification
    Notification <|.. PushNotification
    EmailService ..> EmailNotification : creates
    SMSService ..> SMSNotification : creates
    PushService ..> PushNotification : creates
```
----------------------------------------------------------------------------------


## (3) Singleton

*The Singleton Pattern*
    ensures a class has only one instance, and provides a global point of accesst to it.

**Quick Hints**
- *One and only one!*
    Guarantees a signle instance for the lifetime of your app.
- *Private constructor!*
    Prevents others from creating new instances.
- *Static instance!*
    Holds the single instance in a static variable.
- *Global access!*
    Holds the single instace in a static variable.
- *Lazy or eager?*
    Create the instance when needed(lazy) or at startup(eager).
- *Thread safety matters!*
    Be carefull in muli-threaded environments.

**Mnemonic**
*There can be only one!*

**Analogy**
*Like the captain of a ship: there's only one captain and everyone knows how to reach them.*

**UML Class Diagram**
> Real-world example: Application-wide logger — one instance, accessible globally

```mermaid
classDiagram
    class AppLogger {
        -instance: AppLogger$
        -logFilePath: String
        -AppLogger()
        +getInstance() AppLogger$
        +info(message: String)
        +warn(message: String)
        +error(message: String)
        +debug(message: String)
    }
```
-----------------------------------------------------------------------------------


## (4) State

*The State Pattern*
    allow an object to alter its behaviour when its internal
    state changes. The object will appear to change its class.

**Quick Hints**
- *Encapsulate state-specific behaviour!*
    Put state-dependent code in seperate state classes.
- *Context delegated to state!*
    The context object delegates behavior to the current state object.
- *Change the state, change the behavior!*
    Swap the state object to change how to context behaves.
- *No more giant if/else or switch!*
    Replace conditional logic with polymorphism.
- *State transitions are explicit!*
    State objects can change the context's state

**Mnemonic**
*I change my mind(behavior) when my state changes!*

**Analogy**
*Like a vending machine: its behavior changes depending on weather you've inserted money, selected a product, or it's out of stock*

**UML Class Diagram**
> Real-world example: E-commerce order lifecycle (Pending → Processing → Shipped → Delivered)

```mermaid
classDiagram
    class Order {
        -state: OrderState
        -orderId: String
        +setState(state: OrderState)
        +next()
        +cancel()
        +getStatus() String
    }
    class OrderState {
        <<interface>>
        +next(order: Order)
        +cancel(order: Order)
        +getStatus() String
    }
    class PendingState {
        +next(order: Order)
        +cancel(order: Order)
        +getStatus() String
    }
    class ProcessingState {
        +next(order: Order)
        +cancel(order: Order)
        +getStatus() String
    }
    class ShippedState {
        +next(order: Order)
        +cancel(order: Order)
        +getStatus() String
    }
    class DeliveredState {
        +next(order: Order)
        +cancel(order: Order)
        +getStatus() String
    }
    Order o--> OrderState
    OrderState <|.. PendingState
    OrderState <|.. ProcessingState
    OrderState <|.. ShippedState
    OrderState <|.. DeliveredState
```
-----------------------------------------------------------------------------------


## (5) Observer

*The Observer Pattern*
    defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**Quick Hints**
- *One-to-many relationship!*
    When one object changes, all dependents are notified.
- *Loose coupling!*
    Observers and subjects are loosely coupled.
- *Push or pull updates!*
    The subject can push updates to observers or let them pull the data.
- *Dynamic subscription!*
    Observers can subscribe or unsubscribe at runtime.
- *Encapsulate the core!*
    The subject encapsulates the core logic, while observers handle dependent behavior.

**Mnemonic**
*"I’ll let you know when I change!"*

**Analogy**
*Like a news agency: when news is published (subject), all subscribers (observers) are notified and receive the update.*

**UML Class Diagram**
> Real-world example: Stock market — brokers, alerts, and bots react to price changes

```mermaid
classDiagram
    class StockMarket {
        -observers: List~StockObserver~
        -symbol: String
        -price: float
        +attach(o: StockObserver)
        +detach(o: StockObserver)
        +notifyObservers()
        +updatePrice(price: float)
    }
    class StockObserver {
        <<interface>>
        +update(symbol: String, price: float)
    }
    class Broker {
        -name: String
        +update(symbol: String, price: float)
    }
    class PriceAlert {
        -threshold: float
        +update(symbol: String, price: float)
        +sendAlert()
    }
    class TradingBot {
        -strategy: String
        +update(symbol: String, price: float)
        +executeTrade()
    }
    StockMarket o--> StockObserver : notifies
    StockObserver <|.. Broker
    StockObserver <|.. PriceAlert
    StockObserver <|.. TradingBot
```
-----------------------------------------------------------------------------------


## (6) Decorator

*The Decorator Pattern*
    attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

**Quick Hints**
- *Wrap to extend!*  
    Add new behavior by wrapping objects with decorators.
- *Flexible combinations!*  
    Stack multiple decorators for different combinations of features.
- *Favors composition over inheritance!*  
    Use composition to add functionality, not inheritance.
- *Same interface!*  
    Decorators and components share the same interface.
- *Transparent to client!*  
    Client code can use decorated and undecorated objects interchangeably.

**Mnemonic**
*"I’ll dress you up with new features!"*

**Analogy**
*Like adding toppings to a pizza: each topping (decorator) adds new flavor (behavior) to the base pizza (component).*

**UML Class Diagram**
> Real-world example: Coffee shop — dynamically add milk, mocha, whipped cream to any beverage

```mermaid
classDiagram
    class Beverage {
        <<abstract>>
        #description: String
        +getDescription() String
        +getCost() float
    }
    class Espresso {
        +getDescription() String
        +getCost() float
    }
    class HouseBlend {
        +getDescription() String
        +getCost() float
    }
    class CondimentDecorator {
        <<abstract>>
        -beverage: Beverage
        +CondimentDecorator(b: Beverage)
        +getDescription() String
        +getCost() float
    }
    class Milk {
        +getDescription() String
        +getCost() float
    }
    class Mocha {
        +getDescription() String
        +getCost() float
    }
    class WhippedCream {
        +getDescription() String
        +getCost() float
    }
    Beverage <|-- Espresso
    Beverage <|-- HouseBlend
    Beverage <|-- CondimentDecorator
    CondimentDecorator o--> Beverage : wraps
    CondimentDecorator <|-- Milk
    CondimentDecorator <|-- Mocha
    CondimentDecorator <|-- WhippedCream
```
-----------------------------------------------------------------------------------


## (7) Builder

*The Builder Pattern*
    separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Quick Hints**
- *Step-by-step construction!*  
    Build objects piece by piece.
- *Different representations!*  
    Same process, different results.
- *Director controls the process!*  
    The director tells the builder what to do.
- *Encapsulate construction logic!*  
    Builder hides the details of how parts are assembled.

**Mnemonic**
*"I’ll build it your way!"*

**Analogy**
*Like ordering a custom sandwich: you choose the ingredients, the builder assembles it step by step.*

**UML Class Diagram**
> Real-world example: House construction — director drives the build, builders vary the material

```mermaid
classDiagram
    class ConstructionDirector {
        -builder: HouseBuilder
        +setBuilder(b: HouseBuilder)
        +buildBasicHouse()
        +buildLuxuryHouse()
    }
    class HouseBuilder {
        <<interface>>
        +buildFoundation()
        +buildWalls()
        +buildRoof()
        +buildGarage()
        +buildPool()
        +getHouse() House
    }
    class WoodenHouseBuilder {
        -house: House
        +buildFoundation()
        +buildWalls()
        +buildRoof()
        +buildGarage()
        +buildPool()
        +getHouse() House
    }
    class BrickHouseBuilder {
        -house: House
        +buildFoundation()
        +buildWalls()
        +buildRoof()
        +buildGarage()
        +buildPool()
        +getHouse() House
    }
    class House {
        +foundation: String
        +walls: String
        +roof: String
        +hasGarage: bool
        +hasPool: bool
    }
    ConstructionDirector o--> HouseBuilder
    HouseBuilder <|.. WoodenHouseBuilder
    HouseBuilder <|.. BrickHouseBuilder
    WoodenHouseBuilder ..> House : creates
    BrickHouseBuilder ..> House : creates
```
-----------------------------------------------------------------------------------


## (8) Memento

*The Memento Pattern*
    captures and externalizes an object’s internal state without violating encapsulation, so the object can be restored to this state later.

**Quick Hints**
- *Save and restore state!*  
    Take snapshots of an object’s state.
- *Encapsulation preserved!*  
    State is stored without exposing internals.
- *Caretaker manages mementos!*  
    Caretaker keeps track of saved states.
- *Undo/redo functionality!*  
    Useful for undo operations.

**Mnemonic**
*"I’ll remember so you can go back!"*

**Analogy**
*Like a save point in a video game: you can restore to a previous state if needed.*

**UML Class Diagram**
> Real-world example: Text editor undo/redo — each save captures a snapshot of content

```mermaid
classDiagram
    class TextEditor {
        -content: String
        -cursorPosition: int
        +type(text: String)
        +delete(chars: int)
        +save() EditorMemento
        +restore(m: EditorMemento)
        +getContent() String
    }
    class EditorMemento {
        -content: String
        -cursorPosition: int
        +getContent() String
        +getCursorPosition() int
    }
    class EditorHistory {
        -history: Stack~EditorMemento~
        +backup(editor: TextEditor)
        +undo(editor: TextEditor)
        +canUndo() bool
    }
    TextEditor ..> EditorMemento : creates
    EditorHistory o--> EditorMemento : stores
    EditorHistory --> TextEditor
```
-----------------------------------------------------------------------------------


## (9) Visitor

*The Visitor Pattern*
    lets you define a new operation without changing the classes of the elements on which it operates.

**Quick Hints**
- *Separate algorithm from object structure!*  
    Visitor adds new operations to existing objects.
- *Double dispatch!*  
    Visitor and element cooperate to select the right method.
- *Easy to add new operations!*  
    Add new functionality without modifying element classes.
- *Harder to add new element types!*  
    Must update visitor for new elements.

**Mnemonic**
*"I’ll visit and do something new!"*

**Analogy**
*Like a tax auditor visiting different businesses: each business lets the auditor perform a specific operation.*

**UML Class Diagram**
> Real-world example: Shopping cart — apply standard tax or holiday tax to different item types

```mermaid
classDiagram
    class TaxVisitor {
        <<interface>>
        +visitFood(item: FoodItem) float
        +visitElectronics(item: ElectronicsItem) float
        +visitClothing(item: ClothingItem) float
    }
    class StandardTax {
        +visitFood(item: FoodItem) float
        +visitElectronics(item: ElectronicsItem) float
        +visitClothing(item: ClothingItem) float
    }
    class HolidayTax {
        +visitFood(item: FoodItem) float
        +visitElectronics(item: ElectronicsItem) float
        +visitClothing(item: ClothingItem) float
    }
    class ShopItem {
        <<interface>>
        +accept(v: TaxVisitor) float
        +getPrice() float
    }
    class FoodItem {
        -price: float
        +accept(v: TaxVisitor) float
        +getPrice() float
    }
    class ElectronicsItem {
        -price: float
        +accept(v: TaxVisitor) float
        +getPrice() float
    }
    class ClothingItem {
        -price: float
        +accept(v: TaxVisitor) float
        +getPrice() float
    }
    TaxVisitor <|.. StandardTax
    TaxVisitor <|.. HolidayTax
    ShopItem <|.. FoodItem
    ShopItem <|.. ElectronicsItem
    ShopItem <|.. ClothingItem
    FoodItem ..> TaxVisitor : accepts
    ElectronicsItem ..> TaxVisitor : accepts
    ClothingItem ..> TaxVisitor : accepts
```
-----------------------------------------------------------------------------------

## (10) Composite


*The Composite Pattern*
    lets you compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions uniformly.

**Quick Hints**
- *Tree structure!*  
    Organize objects in a hierarchy.
- *Uniform treatment!*  
    Treat leaves and composites the same way.
- *Recursive operations!*  
    Operations apply to both individual and composite objects.
- *Simplifies client code!*  
    Client doesn’t need to distinguish between single and grouped objects.

**Mnemonic**
*"I’m made of parts, but you can treat me as one!"*

**Analogy**
*Like a folder system: folders can contain files or other folders, and you can perform actions on both.*

**UML Class Diagram**
> Real-world example: File system — files and folders treated uniformly; getSize() works on both

```mermaid
classDiagram
    class FileSystemItem {
        <<interface>>
        +getName() String
        +getSize() long
        +display(indent: String)
    }
    class File {
        -name: String
        -size: long
        +getName() String
        +getSize() long
        +display(indent: String)
    }
    class Folder {
        -name: String
        -children: List~FileSystemItem~
        +getName() String
        +getSize() long
        +display(indent: String)
        +add(item: FileSystemItem)
        +remove(item: FileSystemItem)
    }
    FileSystemItem <|.. File
    FileSystemItem <|.. Folder
    Folder o--> FileSystemItem : contains
```
-----------------------------------------------------------------------------------

## (11) Iterator


*The Iterator Pattern*
    provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

**Quick Hints**
- *Traverse collections!*  
    Access elements one at a time.
- *No need to know structure!*  
    Client doesn’t care how the collection is built.
- *Multiple traversals!*  
    Can have multiple iterators for the same collection.

**Mnemonic**
*"I’ll show you one item at a time!"*

**Analogy**
*Like flipping through a playlist: you see each song in order.*

**UML Class Diagram**
> Real-world example: Music app playlist — iterate songs without exposing internal list structure

```mermaid
classDiagram
    class MusicIterator {
        <<interface>>
        +hasNext() bool
        +next() Song
        +reset()
    }
    class MusicCollection {
        <<interface>>
        +createIterator() MusicIterator
    }
    class Song {
        +title: String
        +artist: String
        +durationSecs: int
    }
    class Playlist {
        -songs: List~Song~
        -name: String
        +addSong(song: Song)
        +createIterator() MusicIterator
    }
    class PlaylistIterator {
        -playlist: Playlist
        -index: int
        +hasNext() bool
        +next() Song
        +reset()
    }
    MusicIterator <|.. PlaylistIterator
    MusicCollection <|.. Playlist
    Playlist ..> PlaylistIterator : creates
    PlaylistIterator --> Playlist
```
-----------------------------------------------------------------------------------


## (12) Proxy

*The Proxy Pattern*
    provides a surrogate or placeholder for another object to control access to it.

**Quick Hints**
- *Control access!*  
    Proxy stands in for the real object.
- *Add extra logic!*  
    Proxies can add security, caching, or logging.
- *Same interface!*  
    Proxy and real subject share the same interface.

**Mnemonic**
*"Talk to my representative!"*

**Analogy**
*Like a receptionist: you interact with them instead of directly with the boss.*

**UML Class Diagram**
> Real-world example: Image gallery — proxy defers loading heavy images until they are displayed

```mermaid
classDiagram
    class Image {
        <<interface>>
        +display()
        +getWidth() int
        +getHeight() int
    }
    class RealImage {
        -filename: String
        -width: int
        -height: int
        -loadFromDisk()
        +display()
        +getWidth() int
        +getHeight() int
    }
    class ImageProxy {
        -filename: String
        -realImage: RealImage
        +display()
        +getWidth() int
        +getHeight() int
    }
    class ImageGallery {
        -images: List~Image~
        +addImage(image: Image)
        +displayAll()
    }
    Image <|.. RealImage
    Image <|.. ImageProxy
    ImageProxy --> RealImage : loads lazily
    ImageGallery o--> Image
```
-----------------------------------------------------------------------------------


## (13) Facade

*The Facade Pattern*
    provides a unified interface to a set of interfaces in a subsystem, making it easier to use.

**Quick Hints**
- *Simplify complexity!*  
    Facade hides the subsystem’s complexity.
- *One-stop shop!*  
    Offers a simple interface for complex operations.
- *Decouples client from subsystem!*  
    Client interacts only with the facade.

**Mnemonic**
*"I’ll make it easy for you!"*

**Analogy**
*Like a universal remote: one remote controls many devices.*

**UML Class Diagram**
> Real-world example: Home theater — one facade call starts the TV, sound system, lights, and streaming

```mermaid
classDiagram
    class HomeTheaterFacade {
        -tv: Television
        -soundSystem: SoundSystem
        -streamingPlayer: StreamingPlayer
        -lights: SmartLights
        +watchMovie(title: String)
        +endMovie()
        +listenToMusic(playlist: String)
    }
    class Television {
        +turnOn()
        +turnOff()
        +setInput(input: String)
    }
    class SoundSystem {
        +turnOn()
        +setVolume(level: int)
        +setSurroundSound()
        +turnOff()
    }
    class StreamingPlayer {
        +turnOn()
        +play(title: String)
        +stop()
        +turnOff()
    }
    class SmartLights {
        +dim(level: int)
        +turnOn()
        +turnOff()
    }
    HomeTheaterFacade --> Television
    HomeTheaterFacade --> SoundSystem
    HomeTheaterFacade --> StreamingPlayer
    HomeTheaterFacade --> SmartLights
```
-----------------------------------------------------------------------------------


## (14) Command

*The Command Pattern*
    encapsulates a request as an object, thereby letting you parameterize clients with queues, requests, and operations.

**Quick Hints**
- *Encapsulate requests!*  
    Turn actions into objects.
- *Undo/redo support!*  
    Store commands for undo/redo.
- *Queue and log requests!*  
    Commands can be queued or logged.
- *Decouples sender from receiver!*  
    The invoker doesn’t know the receiver’s details.

**Mnemonic**
*"I’ll take your order and deliver it later!"*

**Analogy**
*Like a remote control: each button is a command object.*

**UML Class Diagram**
> Real-world example: Smart home remote — buttons trigger encapsulated commands, undo is supported

```mermaid
classDiagram
    class RemoteControl {
        -commands: Map~String, Command~
        -history: Stack~Command~
        +registerCommand(name: String, cmd: Command)
        +pressButton(name: String)
        +undoLast()
    }
    class Command {
        <<interface>>
        +execute()
        +undo()
    }
    class LightOnCommand {
        -light: Light
        +execute()
        +undo()
    }
    class LightOffCommand {
        -light: Light
        +execute()
        +undo()
    }
    class ThermostatCommand {
        -thermostat: Thermostat
        -targetTemp: int
        -previousTemp: int
        +execute()
        +undo()
    }
    class Light {
        -location: String
        +on()
        +off()
    }
    class Thermostat {
        +setTemperature(temp: int)
        +getTemperature() int
    }
    RemoteControl o--> Command
    Command <|.. LightOnCommand
    Command <|.. LightOffCommand
    Command <|.. ThermostatCommand
    LightOnCommand --> Light
    LightOffCommand --> Light
    ThermostatCommand --> Thermostat
```
-----------------------------------------------------------------------------------


## (15) Template Method

*The Template Method Pattern*
    defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing its structure.

**Quick Hints**
- *Define the steps!*  
    The base class outlines the algorithm’s steps.
- *Let subclasses fill in the details!*  
    Subclasses override specific steps.
- *No code duplication!*  
    Common code stays in the base class.
- *Control the algorithm!*  
    The template method controls the sequence.

**Mnemonic**
*"I’ll set the recipe, you add the ingredients!"*

**Analogy**
*Like a coffee machine: the process is fixed, but you can choose the type of coffee.*

**UML Class Diagram**
> Real-world example: Report generator — fixed pipeline (fetch → process → format), subclasses define each step

```mermaid
classDiagram
    class ReportGenerator {
        <<abstract>>
        +generate()
        +fetchData()*
        +processData()*
        +formatOutput()*
        +saveToFile()
    }
    class PDFReport {
        +fetchData()
        +processData()
        +formatOutput()
    }
    class ExcelReport {
        +fetchData()
        +processData()
        +formatOutput()
    }
    class CSVReport {
        +fetchData()
        +processData()
        +formatOutput()
    }
    ReportGenerator <|-- PDFReport
    ReportGenerator <|-- ExcelReport
    ReportGenerator <|-- CSVReport
```
-----------------------------------------------------------------------------------


## (16) Compound

*The Compound Pattern*
    combines two or more patterns to solve a recurring or complex design problem. Often used in frameworks and libraries to leverage the strengths of multiple patterns together.

**Quick Hints**
- *Mix and match!*  
    Use several patterns together for robust solutions.
- *Frameworks love it!*  
    Common in UI toolkits and libraries.
- *Synergy of patterns!*  
    Patterns work together to solve bigger problems.

**Mnemonic**
*"Stronger together!"*

**Analogy**
*Like a Swiss Army knife: multiple tools in one package.*

**UML Class Diagram**
> Real-world example: MVC — combines Observer (model notifies views) + Strategy (controller swaps input handling)

```mermaid
classDiagram
    class UserModel {
        -username: String
        -email: String
        -observers: List~Observer~
        +attach(o: Observer)
        +detach(o: Observer)
        +notifyAll()
        +setEmail(email: String)
    }
    class Observer {
        <<interface>>
        +update(model: UserModel)
    }
    class ProfileView {
        +update(model: UserModel)
        +render()
    }
    class DashboardView {
        +update(model: UserModel)
        +render()
    }
    class UserController {
        -model: UserModel
        -inputStrategy: InputStrategy
        +handleUpdateEmail(email: String)
        +setInputStrategy(s: InputStrategy)
    }
    class InputStrategy {
        <<interface>>
        +validate(input: String) bool
    }
    class StrictValidation {
        +validate(input: String) bool
    }
    class LenientValidation {
        +validate(input: String) bool
    }
    UserModel o--> Observer : notifies
    Observer <|.. ProfileView
    Observer <|.. DashboardView
    UserController --> UserModel
    UserController o--> InputStrategy
    InputStrategy <|.. StrictValidation
    InputStrategy <|.. LenientValidation
```
-----------------------------------------------------------------------------------

## (17) Visitor

*The Visitor Pattern*
    lets you define a new operation without changing the classes of the elements on which it operates.

**Quick Hints**
- *Separate algorithm from object structure!*  
    Visitor adds new operations to existing objects.
- *Double dispatch!*  
    Visitor and element cooperate to select the right method.
- *Easy to add new operations!*  
    Add new functionality without modifying element classes.
- *Harder to add new element types!*  
    Must update visitor for new elements.

**Mnemonic**
*"I’ll visit and do something new!"*

**Analogy**
*Like a tax auditor visiting different businesses: each business lets the auditor perform a specific operation.*

**UML Class Diagram**
> Real-world example: Drawing app — shapes accept visitors for area calculation and XML export without modification

```mermaid
classDiagram
    class ShapeVisitor {
        <<interface>>
        +visitCircle(c: Circle)
        +visitRectangle(r: Rectangle)
        +visitTriangle(t: Triangle)
    }
    class AreaCalculator {
        -totalArea: float
        +visitCircle(c: Circle)
        +visitRectangle(r: Rectangle)
        +visitTriangle(t: Triangle)
        +getTotalArea() float
    }
    class XMLExporter {
        -xml: String
        +visitCircle(c: Circle)
        +visitRectangle(r: Rectangle)
        +visitTriangle(t: Triangle)
        +getXML() String
    }
    class Shape {
        <<interface>>
        +accept(v: ShapeVisitor)
    }
    class Circle {
        -radius: float
        +accept(v: ShapeVisitor)
    }
    class Rectangle {
        -width: float
        -height: float
        +accept(v: ShapeVisitor)
    }
    class Triangle {
        -base: float
        -height: float
        +accept(v: ShapeVisitor)
    }
    ShapeVisitor <|.. AreaCalculator
    ShapeVisitor <|.. XMLExporter
    Shape <|.. Circle
    Shape <|.. Rectangle
    Shape <|.. Triangle
    Circle ..> ShapeVisitor : accepts
    Rectangle ..> ShapeVisitor : accepts
    Triangle ..> ShapeVisitor : accepts
```
-----------------------------------------------------------------------------------


## (18) Null Object

*The Null Object Pattern*
    provides an object as a surrogate for the lack of an object of a given type. The null object implements the expected interface but does nothing.

**Quick Hints**
- *Avoid null checks!*  
    Use a do-nothing object instead of null.
- *Same interface!*  
    Null object implements the same interface as real objects.
- *Safe defaults!*  
    Prevents null pointer exceptions.

**Mnemonic**
*"I’m here, but I do nothing!"*

**Analogy**
*Like a silent partner: present, but never participates.*

**UML Class Diagram**
> Real-world example: Logging — NullLogger eliminates null checks throughout the codebase

```mermaid
classDiagram
    class Logger {
        <<abstract>>
        +log(message: String)
        +error(message: String)
        +warn(message: String)
        +isNull() bool
    }
    class ConsoleLogger {
        +log(message: String)
        +error(message: String)
        +warn(message: String)
        +isNull() bool
    }
    class FileLogger {
        -filePath: String
        +log(message: String)
        +error(message: String)
        +warn(message: String)
        +isNull() bool
    }
    class NullLogger {
        +log(message: String)
        +error(message: String)
        +warn(message: String)
        +isNull() bool
    }
    class Application {
        -logger: Logger
        +setLogger(logger: Logger)
        +run()
    }
    Logger <|-- ConsoleLogger
    Logger <|-- FileLogger
    Logger <|-- NullLogger
    Application o--> Logger
```
-----------------------------------------------------------------------------------


## (19) Chain of Responsibility

*The Chain of Responsibility Pattern*
    lets you pass requests along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain.

**Quick Hints**
- *Decouple sender and receiver!*  
    Sender doesn’t know which handler will process the request.
- *Flexible chains!*  
    Handlers can be added, removed, or reordered.
- *Each handler gets a chance!*  
    Each handler can process or pass the request.

**Mnemonic**
*"Pass it along until someone handles it!"*

**Analogy**
*Like customer service escalation: your request moves up the chain until someone resolves it.*

**UML Class Diagram**
> Real-world example: ATM cash dispenser — request passes through handlers for each bill denomination

```mermaid
classDiagram
    class CashHandler {
        <<abstract>>
        -next: CashHandler
        +setNext(handler: CashHandler) CashHandler
        +handle(amount: int)
        #dispense(bills: int)*
    }
    class HundredBillHandler {
        #dispense(bills: int)
    }
    class FiftyBillHandler {
        #dispense(bills: int)
    }
    class TwentyBillHandler {
        #dispense(bills: int)
    }
    class TenBillHandler {
        #dispense(bills: int)
    }
    CashHandler <|-- HundredBillHandler
    CashHandler <|-- FiftyBillHandler
    CashHandler <|-- TwentyBillHandler
    CashHandler <|-- TenBillHandler
    CashHandler o--> CashHandler : next
```
-----------------------------------------------------------------------------------


## (20) Prototype


*The Prototype Pattern*
    specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.

**Quick Hints**
- *Clone, don’t build!*  
    Create new objects by copying (cloning) an existing object.
- *Avoids subclassing for new objects!*  
    No need to write code to create each new object from scratch.
- *Add or remove objects at runtime!*  
    New prototypes can be registered and cloned as needed.
- *Reduces the need for subclasses!*  
    Use prototypes instead of subclassing for slight variations.
- *Deep vs. shallow copy!*  
    Decide if you need a deep or shallow clone.

**Mnemonic**
*"Copy me!"*

**Analogy**
*Like making a key copy: you use an existing key (the prototype) to create a new one, rather than forging a new key from scratch.*

**UML Class Diagram**
> Real-world example: Game character spawning — clone pre-configured prototypes instead of rebuilding from scratch

```mermaid
classDiagram
    class GameCharacter {
        <<interface>>
        +clone() GameCharacter
        +getInfo() String
    }
    class Warrior {
        -name: String
        -level: int
        -weapon: String
        -health: int
        +clone() GameCharacter
        +setName(name: String)
        +getInfo() String
    }
    class Mage {
        -name: String
        -level: int
        -spell: String
        -mana: int
        +clone() GameCharacter
        +setName(name: String)
        +getInfo() String
    }
    class CharacterRegistry {
        -prototypes: Map~String, GameCharacter~
        +register(key: String, c: GameCharacter)
        +spawn(key: String) GameCharacter
    }
    GameCharacter <|.. Warrior
    GameCharacter <|.. Mage
    CharacterRegistry o--> GameCharacter : stores prototypes
    CharacterRegistry ..> GameCharacter : clones
```
-----------------------------------------------------------------------------------


## (21) Bridge

*The Bridge Pattern*
    decouples an abstraction from its implementation so that the two can vary independently.

**Quick Hints**
- *Separate abstraction from implementation!*  
    Both can change without affecting each other.
- *Use composition, not inheritance!*  
    Abstraction holds a reference to the implementor.
- *Extend independently!*  
    Add new abstractions and implementations freely.

**Mnemonic**
*"I’ll connect you without tying you down!"*

**Analogy**
*Like a TV remote: the remote (abstraction) works with different brands of TVs (implementations) without changing the remote.*

**UML Class Diagram**
> Real-world example: Remote control + devices — add new remotes or device brands independently

```mermaid
classDiagram
    class RemoteControl {
        #device: Device
        +RemoteControl(device: Device)
        +togglePower()
        +volumeUp()
        +volumeDown()
    }
    class AdvancedRemoteControl {
        +mute()
        +setChannel(num: int)
    }
    class Device {
        <<interface>>
        +isEnabled() bool
        +enable()
        +disable()
        +getVolume() int
        +setVolume(v: int)
        +getChannel() int
        +setChannel(c: int)
    }
    class TV {
        -on: bool
        -volume: int
        -channel: int
        +isEnabled() bool
        +enable()
        +disable()
        +getVolume() int
        +setVolume(v: int)
        +getChannel() int
        +setChannel(c: int)
    }
    class Radio {
        -on: bool
        -volume: int
        -frequency: int
        +isEnabled() bool
        +enable()
        +disable()
        +getVolume() int
        +setVolume(v: int)
        +getChannel() int
        +setChannel(c: int)
    }
    RemoteControl <|-- AdvancedRemoteControl
    RemoteControl o--> Device
    Device <|.. TV
    Device <|.. Radio
```
-----------------------------------------------------------------------------------


## (22) Flyweight

*The Flyweight Pattern*
    uses sharing to support large numbers of fine-grained objects efficiently.

**Quick Hints**
- *Share common state!*  
    Store shared data externally to reduce memory usage.
- *Separate intrinsic and extrinsic state!*  
    Intrinsic is shared, extrinsic is unique per object.
- *Great for lots of similar objects!*  
    Useful in graphics, text editors, etc.

**Mnemonic**
*"I’m small and shared!"*

**Analogy**
*Like chess pieces: many pieces share the same type, only position is unique.*

**UML Class Diagram**
> Real-world example: Game map tiles — thousands of tiles share appearance data; only position is unique per tile

```mermaid
classDiagram
    class TileAppearance {
        -texture: String
        -color: String
        -isPassable: bool
        +render(x: int, y: int)
    }
    class TileFactory {
        -cache: Map~String, TileAppearance~
        +getTile(type: String) TileAppearance
        +getCachedCount() int
    }
    class MapTile {
        -x: int
        -y: int
        -appearance: TileAppearance
        +draw()
        +isWalkable() bool
    }
    class GameMap {
        -tiles: MapTile[]
        +loadMap(data: String[][])
        +render()
    }
    TileFactory o--> TileAppearance : caches shared state
    MapTile --> TileAppearance : uses shared state
    GameMap o--> MapTile
    GameMap --> TileFactory
```
-----------------------------------------------------------------------------------


## (23) Interpreter

*The Interpreter Pattern*
    defines a representation for a language’s grammar along with an interpreter that uses the representation to interpret sentences in the language.

**Quick Hints**
- *Grammar and interpretation!*  
    Represent grammar rules as classes.
- *Parse and evaluate!*  
    Interpreter parses and evaluates sentences.
- *Easy to extend!*  
    Add new grammar rules by adding new classes.

**Mnemonic**
*"I’ll translate your language!"*

**Analogy**
*Like a calculator: interprets and evaluates mathematical expressions.*

**UML Class Diagram**
> Real-world example: Math expression parser — builds and evaluates expression trees like (3 + 5) * 2

```mermaid
classDiagram
    class Expression {
        <<interface>>
        +interpret() int
    }
    class NumberExpression {
        -value: int
        +interpret() int
    }
    class AddExpression {
        -left: Expression
        -right: Expression
        +interpret() int
    }
    class SubtractExpression {
        -left: Expression
        -right: Expression
        +interpret() int
    }
    class MultiplyExpression {
        -left: Expression
        -right: Expression
        +interpret() int
    }
    class ExpressionParser {
        +parse(expression: String) Expression
    }
    Expression <|.. NumberExpression
    Expression <|.. AddExpression
    Expression <|.. SubtractExpression
    Expression <|.. MultiplyExpression
    AddExpression o--> Expression : left/right
    SubtractExpression o--> Expression : left/right
    MultiplyExpression o--> Expression : left/right
    ExpressionParser ..> Expression : creates
```
-----------------------------------------------------------------------------------


## (24) Mediator

*The Mediator Pattern*
    defines an object that encapsulates how a set of objects interact, promoting loose coupling by keeping objects from referring to each other explicitly.

**Quick Hints**
- *Centralize communication!*  
    Mediator handles interactions between objects.
- *Loose coupling!*  
    Objects communicate through the mediator, not directly.
- *Simplifies object relationships!*  
    Reduces dependencies between objects.

**Mnemonic**
*"I’ll coordinate everyone’s conversation!"*

**Analogy**
*Like an air traffic controller: coordinates planes so they don’t talk to each other directly.*
**UML Class Diagram**
> Real-world example: Chat room — users never message each other directly; the room mediates all communication

```mermaid
classDiagram
    class ChatMediator {
        <<interface>>
        +sendMessage(msg: String, sender: User)
        +addUser(user: User)
    }
    class ChatRoom {
        -users: List~User~
        +sendMessage(msg: String, sender: User)
        +addUser(user: User)
    }
    class User {
        #mediator: ChatMediator
        #name: String
        +User(mediator: ChatMediator, name: String)
        +send(message: String)
        +receive(message: String, from: String)
    }
    class RegularUser {
        +send(message: String)
        +receive(message: String, from: String)
    }
    class AdminUser {
        +send(message: String)
        +receive(message: String, from: String)
        +broadcast(message: String)
    }
    ChatMediator <|.. ChatRoom
    User <|-- RegularUser
    User <|-- AdminUser
    User o--> ChatMediator
    ChatRoom o--> User
```-----------------------------------------------------------------------------------


## (25) Adapter

*The Adapter Pattern*
    allows objects with incompatible interfaces to work together. Adapter wraps an existing class with a new interface.

**Quick Hints**
- *Convert the interface!*  
    Adapter makes one interface look like another.
- *Wrap and delegate!*  
    Adapter wraps the adaptee and delegates calls.
- *Client sees only the target interface!*  
    The client uses the adapter, not the adaptee directly.
- *Two main types:*  
    Object Adapter (uses composition), Class Adapter (uses inheritance).
- *Use when you can’t change the existing code!*  
    Adapter lets you reuse code without modifying it.

**Mnemonic**
*"I’ll translate for you!"*

**Analogy**
*Like a power plug adapter: lets your device (client) use a foreign socket (adaptee) by converting the interface.*

**UML Class Diagram**
> Real-world example: Payment gateway integration — adapt Stripe and PayPal SDKs to a unified interface

```mermaid
classDiagram
    class PaymentProcessor {
        <<interface>>
        +processPayment(amount: float, currency: String) bool
        +refund(transactionId: String) bool
    }
    class StripeAdapter {
        -stripe: StripeClient
        +processPayment(amount: float, currency: String) bool
        +refund(transactionId: String) bool
    }
    class StripeClient {
        +charge(cents: int, currency: String) Response
        +reverse(chargeId: String) Response
    }
    class PayPalAdapter {
        -paypal: PayPalSDK
        +processPayment(amount: float, currency: String) bool
        +refund(transactionId: String) bool
    }
    class PayPalSDK {
        +executePayment(usd: float) Result
        +voidTransaction(id: String) Result
    }
    class CheckoutService {
        -processor: PaymentProcessor
        +setProcessor(p: PaymentProcessor)
        +completeOrder(amount: float)
    }
    PaymentProcessor <|.. StripeAdapter
    PaymentProcessor <|.. PayPalAdapter
    StripeAdapter --> StripeClient : delegates
    PayPalAdapter --> PayPalSDK : delegates
    CheckoutService o--> PaymentProcessor
```



Singleton: Ensures a single instance of a class.
Factory: Provides an interface for object creation, letting subclasses decide the class to instantiate.
Builder: Separates complex object construction from its representation.
Abstract Factory: Creates families of related objects. 

Facade: Simplifies a complex system interface.
Decorator: Adds behaviors dynamically by wrapping an object.
Adapter: Allows incompatible interfaces to work together.
Proxy: Provides a substitute for another object to control access. 

Observer: Defines a one-to-many dependency for state change notifications.
Strategy: Defines interchangeable algorithms.
Command: Encapsulates a request as an object.
Iterator: Provides sequential traversal of collection elements.
State: Allows behavior change based on internal state. 
