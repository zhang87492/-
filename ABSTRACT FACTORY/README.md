# 感受：

1. 将整个代码抽象为一个大型模板盖章。在面对不同需求时，只需要替换其中的传入产品类名即可。

# 问题：

1. 画出通用类图（20分，并说明各个类的作用）
2. 实战例子.提出两个抽象工厂的例子，实现它，并说明其中各个类扮演的角色。。(20分)
3. 有什么优点和缺点。（4项，20分）
4. 适用性和意图（5点，20分)

# 答案
1. 实战例子.提出两个抽象工厂的例子，并实现它。

   - 同样的前端，不同的后台数据库实现。可参考代码。

     [MazeFactory.py](MazeFactory.py)
     
- 设计模式书籍里的迷宫，具体实现可参考代码 [EMployeeDao.py](EMployeeDao.py)
  
2. 画出通用类图。![AbstractFactory](assets/Main.jpg)

    - AbstractFactory:
      
      * 声明一个创建抽象产品对象的操作接口。
      
    - ConcreteFactory:
      
      * 实现创建具体产品对象的操作。
      
    - AbstractProduct:
      
      * 为一类产品对象声明一个接口。
      
    - ConcreteProduct:
      * 定义一个将被相应的具体工厂创建的产品对象。
      * 实现AbstractProduct的接口。
      
    - Client：
      
      * 仅使用由AbstractFactory和AbstractProduct类声明的接口。
      
    - 抽象工厂里的例子
    
  * 迷宫游戏的角色说明
        + 代码里面没有设定AbstractFactory和ConcreteFactory。也可以说是client或者main就是这个角色。
        + AbstractProduct就是基础的迷宫设置类Maze
        + ProductA就是AbstractProduct的一个产品对象。
      * 数据库连接类
        + AbstractFactory
          - IDBFactory
        + ConcreteFactory
          - MysqlDBFactory和OraclDBFactory
        + ABstractProduct
          - IDBCommand和IDBReader和IDBConnection
        + ConcreProduct
          - OraclCommand和OraclReader和OraclConnect
          - MysqlCommand和MysqlReader和MysqlConnect
3. 有什么优点和缺点。
   + （优点）**它分离了具体的类**  客户通过他们的抽象接口操纵具体的实例。产品的类名也在具体的工厂实现中被分离；它们不出现在客户代码中。
     + 就是面向接口编程
   + （优点）**它使得易于交换产品系列** 一个具体工厂类在一个应用中仅**出现一次，即在它初始化的时候**。这使得改变一个应用的具体工厂变得很容易。它只需改变具体的工厂即可使用不同的配置。
   + （优点）**它有利于产品的一致性** 当一个系列中的产品对象被设计成一起工作时，一个应用一次只能使用同一个系列中的产品。AbstractFactory很容易实现这一点。
   + （缺点）**难以支持新种类的产品** 难以扩展抽象工厂以生产新种类的产品。
4. 适用性和意图。
   + 意图：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
   + 适用性：
     + 一个系统要独立于它的产品的创建、组合和表示时。 即系统的运行部分可通过抽象，转化为几个接口的组合时。当然这句话不能反推回去。
     + 一个系统要由多个产品系列中的一个来配置时。
     + 当你要强调一系列相关的产品对象的设计以便进行联合使用时。（即一致性）
     + 当你提供一个产品类库，而只想显示它们的接口而不是实现时。（抽象为面向接口编程。）


