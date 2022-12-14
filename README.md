# 机器学习中的概率统计
学习概率统计的时候结合具体场景也许有更深入理解。  
这里结合机器学习和Python语言，温习概率统计知识。  

### 条件概率
研究独立事件概率的意义不大，实际生活中也很少独立事件。  
给定某事件发生概率，在此基础上研究另一事件的发生概率。  

可以理解为两个事件发生概率的交集，即同时发生的概率：  
A事件发生的概率乘以A事件发生前提下B事件的发生概率。  
数学表达为P(AB)=P(B|A)P(A)或P(B|A)=P(AB)/P(A)  

### 独立事件
一般情况下某个事件的独立概率值和条件概率值不同。  
但如果相同就意味着两事件之间没有影响，即相独立。  
即P(AB)=P(A)P(B)，一般只有时空无交集才能独立。  

### 全概率公式
全事件的子事件，每次必发生其一且任意两个不会同时发生。  
引入额外事件，将其概率按分配到全事件的所有子事件中去。  
其概率为各子事件条件概率以子事件概率为权重的加权平均。  
其值在子事件与额外事件片的条件概率最小值和最大值之间。  
P(A)=P(B1)P(A|B1)+P(B2)P(A|B2)+...+P(Bn)P(A|Bn)

### 贝叶斯公式
P(Bi|A)=P(ABi)/P(A)=P(Bi)P(A|Bi)/P(A)=  
P(Bi)P(A|Bi)/(P(B1)P(A|B1)+...+P(Bn)P(A|Bn))  
注意它通过如下等式将P(B|A)和P(A|B)联系到了一起：  
* P(AB)=P(B)P(A|B)
* P(A)=(P(B1)P(A|B1)+...+P(Bn)P(A|Bn))

贝叶斯公式的意义在于推断造成A结果的各种B原因的概率。  
作为原因的B可能不止一个，所以一般用P(Bi|A)来表示。  
在由果追因中贝叶斯公式会很有用，基础理论是条件概率。  

### 独立性
独立事件即P(A|B)=P(A)也就是B对A的发生概率没有影响。  
再由P(A|B)的定义，也就是P(AB)/P(B)可以得到：  
P(A|B)=P(A)=P(AB)/P(B) -> P(AB)=P(A)P(B)    

### 不相容
如果AB事件不相容，意味着他们的交集为空，有P(AB)=0  
由于P(A)和P(B)都不为0，所以P(A)P(B)!=0=P(AB)  
因此，不相容的事件AB一定不是独立的事件。    
逻辑上，不相容事件AB中一个发生意味着另一个不发生。  
所以不相容事件相互引入了额外信息，因而不相互独立。  

### 条件独立
前面已经提到，独立事件满足P(AB)=P(A)P(B)  
在以上加入条件C，即P(AB|C)=P(A|C)P(B|C)  

先看P(AB|C)=P(ABC)/P(C)=P(A|BC)P(BC)/P(C)  
=P(A|BC)P(B|C)P(C)/P(C)=P(A|BC)P(B|C)  

再根据条件独立的定义，即P(AB|C)=P(A|C)P(B|C)  
得到P(A|BC)P(B|C)=P(A|C)P(B|C)即P(A|BC)=P(A|C)  
即事件C发生的前提下，事件B是否发生并不影响事件A的发生。  

### 独立与条件独立
假设A事件是第一次抛硬币得到硬币正面向上的结果。  
假设B事件是第二次抛硬币得到硬币正面向上的结果。  
假设C条件是两次抛硬币的结果不可以相同。  
显然AB事件是互不影响的独立事件，满足P(AB)=P(A)P(B)  

但根据以上事件和条件定义，有P(AB|C)=0  
因为AB事件有相同结果，C条件规定两个事件结果不同。  
同时有P(A|C)!=0且P(B|C)!=0
所以有P(AB|C)=0!=P(A|C)P(B|C)!=0

以上结论是，独立与条件独立并没有必然联系。  

### 伯努利实验
实验由一系列小实验组成，且每个小实验只有两种可能结果。  
伯努利实验是一种独立重复实验，如连续抛硬币的实验就是。  

## 离散型随机变量
关注变量的取值，取值对应的概率，和统计特征与度量方法。  

### 分布列
分布列描述离散随机变量的每种取值及其对应的概率。  
还以抛硬币为例，设抛n次，每次结果硬币正面向上概率为p。  
当n足够大时，结果向上的次数和概率的对应关系如下：  
取值 ｜ 0 ｜ 1 ｜ 2 ｜ 其他
p   ｜1/4｜1/2｜1/4｜  0

### 概率质量函数
即PMF，将随机变量的值映射到其概率上，用图形表达其分布。  

### 二项分布
随机变量只有可能取两个值的时候，如抛硬币得到的正反结果。  
连续抛n次，得到对应随机变量值的概率，参考0201的分布图。  
解读方式为：当每抛一次得到正面的概率p为0.25时，抛10次  
得到结果为2的概率最高，大约为0.25，也就是25%左右。  

这里有个发现，即p=0.5时抛10次得到5次正面的概率仅为0.25。  
虽然每抛都有50%可能正面，但抛10次得到5正面的概率不是50%。  
实际上，得不到5次正面和得到5次正面的赔率是3:1，是蛮大的。  
另外要注意的是，得不到5次正面和得到5次反面也不是一回事。  

实际上不论p值如何，得到任意次正面的最大概率始终是0.25左右。  

### 几何分布
几何分布考量的是，连续抛掷硬币到相应次数正面结果的概率。  
如当p为0.5时，抛掷一次得正面的概率就是0.5，二次为0.25。  
而当p为0.25时，抛掷一次得正面的概率就是0.25，类推。  
概率质量函数的图形表达参考0202的Python脚本绘图结果。  

### 泊松分布
n次独立伯努利实验成功的概率为p，是服从二项分布的随机变量。  
当n非常大近无穷而p非常小近零时，泊松分布与二项分布近似。  
泊松分布函数只需要一个参数λ=n*p，查看0206生成的图形。  
可以从图形观察到，随着λ的增大，最大概率值呈下降趋势。  

## 连续随机变量
汽车速度和设备运行时间等，取值于连续区域的随机变量也很普遍。  
离散随机变量有PMF概率质量函数，连续随机变量有概率密度函数PDF。  
单个点的概率密度函数取值不是概率，而是概率律，因此可以大于1。  
一般讨论连续随机变量在一个区域内的取值概率，而不是单点的概率值。  

随机变量的区间概率通过积分计算，概率密度函数有非负性和归一性：  
非负性即对一切x都有概率值大于0，归一性即全部概率值总和为1。  

### 正态分布
正态分布是一种连续随机变量概率分布，在自然和社会现象中普遍存在。  
函数带有两个参数均值和标准差，均值决定位置，标准差决定形态。  
使用norm函数代入loc和scale分别代表均值和标准差，参考0208。  

### 指数分布
一般用来表现到某个事件发生所用的时间，比如一台设备的残值。  
其图形特征是当随机变量超过某个值时概率随变量值增加呈指数递减。  
指数函数只需要一个参数Scale，参考0210和0211的图形和采样。  

### 均匀分布
随机变量在区间loc到loc+scale之间拥有一个恒定值，处处相等。  
参考0212和0213查看均匀分布的函数图形和采样。  

## 多元随机变量
同一个实验结果可能产生多个随机变量，其取值存在相互关联。  
以下从离散型随机变量开始考察多远随机变量的分布。  

### 联合分布
任意一组随机变量都有对应的联合概率值，若干组集合也是同理。  
如果联合分布列包含XY两个随机变量，则任意XiYi有对应的概率值。  
如果两个事件可以映射到XiYi和XjYj那么总概率就是概率值之和。  
最后，如果将联合分布列中的概率汇总结果必然是1，满足归一性。  

### 边缘分布
边缘分布可以看作是联合分布的降维，如XiY1+XiY2+...+XiYn  
如上处理得到的概率即X维度上的边缘概率：X1, X2, ..., Xn  
可以理解为边缘概率只与指定维度的变量，如X自己有关，与Y无关。  
相应的，联合概率的每个概率值由每个维度上的随机概率共同决定。  

### 条件分布
所谓条件可以是已知某个事件的发生或已知某个条件概率的确定值。  
所谓条件分布就是在如上已知条件下随机变量的概率的分布情况。  
例如看Y=y2条件下随机变量的条件分布，首先计算边缘概率P(y2)  
接着计算每个P(xi,y2)/P(y2)的条件概率，结果应该满足归一性。  

### 期望和方差
如果随机变量相互独立，那么他们乘积的期望等于各自期望的乘积。  
同时，独立随机变量各自边缘分布列的乘积等于其联合分布列的值。  
再有，独立随机变量的和的方差等于各变量各自方差的和。  
随机变量的和的期望等于各变量各自期望的和，它不需要独立条件。  

### 量化相关性
如果相关，我们会想了解一个变量变化时另一个变量发生多大变化。  
定量指标是协方差，即各变量偏离各自预期的差，的乘积，的预期。  
多元随机变量的相关性用所有随机变量两两之间的协方差矩阵分析。  

但两组随机变量的相关性大小与协方差值大小之间不存在线性关系。  
不同随机变量组之间的相关系数并不受协方差绝对值的大小影响。  
一组随机变量各乘a后，其协方差值会增加a^2倍，但相关性不变。  

用随机变量除以标准差，即让各随机变量的方差回到 1 来标准化。  
标准化处理后的相关系数值在正负 1 之间，0 表示变量相互独立。  
相关系数越接近 1 表示相关性越大，图像的椭圆越加收紧成直线。  
值为正表示正相关，图像向右上方倾斜，否则负相关向左上方倾斜。  
查看脚本0214到0218的图形和结果了解二元随机变量的分布特征。  

### 独立与相关
需要注意的是，独立并不等于不相关，即协方差为 0 不代表不相关。  
因为协方差只是数字表示特征的概括，而独立性的描述意义更准确。  
具体可以参考脚本0219所计算的协方差、绘制的图形和代码内注释。  

### 多元高斯分布
多元高斯分布可用矩阵表示，包含 N 个样本，每样本 p 个维度。  
例如某校的 N 个学生，每人有身高、体重、学习成绩等 P 个特征。  
当 P=1 也是一种特殊情况，可以将其看作是列为 1 的特殊矩阵。  

多元高斯分布的特征参数包括 p 个维度的均值和 pxp 协方差矩阵。  
当该协方差矩阵中所有非对角线位置上为 0 时，所有特征都不相关。  
查看脚本0220生成的图像了解均值向量和协方差对样本分布的影响。  

多元高斯分布的概率密度函数的关键部分在维度为 2 时即椭圆方程。  
椭圆的高和宽由两个维度上的方差值大小决定，倾斜度由协方差决定。  
椭圆越小边界上的概率值越高，反之椭圆越大边界上的概率值越小。 

可以使用 SciPy 的 linalg 模块分析协方差矩阵并得到其特征值。  
包括二元高斯椭圆分布的长宽比，以及从协方差矩阵得到的特征向量。  
具体可以参考脚本0221所绘制的图形和代码内注释。  

## 参数估计
大数定律和中心极限定理，在概率统计中用大量样本逼近总体的极限。  
蒙特卡洛方法，无偏估计，极大似然估计，含有隐变量的参数估计等。  
EM算法的合理性和有效性，EM算法实际解决高斯混合模型的参数估计。  

### 大数定律
通过计算样本参数来估计总体的目标参数时，样本越大近似效果越好。  
据推导n个独立同分布随机变量的均值方差是单一随机变量方差的1/n。  
当n趋于无穷大时随机变量的均值方差近于0而紧密分布在期望值周围。  

大数定律即，在大样本的情况下，独立同分布的随机变量的样本均值：  
以很大的概率与随机变量的均值非常接近，样本概率很接近实际概率。  
脚本0301和0302模拟：随样本数目增大样本均值接近实际分布期望。  

### 中心极限定理
根据大数定律，每次采样数会影响均值分布形态，采样多则形态高耸。  
为消除采样数量的影响，将采样均值分布形态标准化，引入新的变量：  
Zn=(X1+X2+...+Xn-n*miu)/(sigma\*n^(1/2))  
上式中miu为均值，sigma为方差的平方根，Zn的期望为0，方差为1。  
对于任意随机变量，Zn随样本数增至无穷大收敛于一个标准正态分布。  

中心极限定理的意义是：大量样本独立随机因素的叠加趋近正态分布。  
即不必关心随机变量的分布列或概率密度函数，只要均值和方差即可。  
观察0303脚本的图像了解中心极限定理的模拟和验证。  

### 蒙特卡罗方法
基于大数定律的统计模拟方法，用随机数进行场景模拟和过程仿真。  
可用于近似计算不规则面积体积，模拟随机过程，统计推断未知参数。  
查看0304脚本了解模拟计算圆形面积和Pi值的方法和实际结果。  

### 统计推断
分析已有样本数据并计算特征，如样本方差等，属于描述统计的范畴。  
通过已有样本数据推断总体的未知参数，是这里即将展开的统计推断。  

如果总体包含大量甚至无限个体，抽出1个或n个个体不会影响总体。  
但当总体包含的个体数目不大时，抽样后需要放回，以免影响总体。  
完全由样本决定的量叫做统计量，不依赖其他未知的量或总体参数。  
查看0305和0306脚本了解统计推断总体方差时用n-1而不是n的原因。  

### 极大似然估计
考虑抛硬币的例子：有抛出正面概率为2/5，1/2和3/5的三枚硬币。  
假设抛20次，有13次正面向上，最有可能是以上三枚中的哪枚硬币？  
计算以上场景的概率的数学式：C(20,13)p^13(1-p)^(20-13)  
查看0307脚本和计算结果，并了解相关的计算方法和思路。  

仍以如上场景为例，抛掷k次硬币正面向上xi次的概率只与概率P有关。  
因为概率计算式中其他值已经由k和xi决定，这里把P称作未知参数 $\theta$。  
换句话说，概率质量函数PMF是一个关于未知(待估)参数 $\theta$ 的函数。  
连续做n次如上的相同实验，一串样本值为x1，x2到xn的联合概率为：  
P(x1 | $\theta$ )P(x2 | $\theta$ )...P(xn | $\theta$ )同样由参数 $\theta$ 决定  

所谓似然函数，就是取得一串指定样本的概率值完全由未知参数 $\theta$ 决定。  
对于连续型随机变量，只要把概率质量函数换成概率密度函数f(xi | $\theta$ )。  
之后就是求解 $\theta$ 取值范围内获得已知样本的可能性最大的值。  

对似然函数求导，导数为 0 的 $\theta$ 取值就是极大似然估计值。  
虽然连乘的似然函数求导较难，但可以对似然函数的自然对数函数求导。  
因为连乘的似然函数的单调性与同函数的自然对数函数的单调性一致。  
而连乘似然函数的自然对数函数将连乘变成了连加，简化了求导过程。  
如果存在多个未知参数，则对每个未知参数求解偏导数即可。  

### 极似实例
极大似然估计实例，抛掷10次得到6次正面的未知概率极似值应为.6  
计算方法如下，注意自然对数的导数为ln $\theta$ = 1 / $\theta$  
似然函数函数为: $\theta$ ^6 \* (1 - $\theta$)^4  
似然函数的对数函数: 6\*ln $\theta$ + 4\*ln(1 - $\theta$)  
对以上函数求导并令其为0: (10 \* $\theta$ - 6)/( $\theta$ * (1 - $\theta$))() = 0  

### 隐变量
如果似然函数更为复杂，包含隐藏变量，可以用迭代的最大期望算法。  
例如抛掷两个正面概率未知的硬币，或者混合男女性别情况下测量身高。  
即在n组抽样中，我们不清楚每组中每次抽样的硬币是哪个或性别如何。  
但只要每组之间使用同样的抽样类型，就可以用迭代法求解极似参数。  
具体参考脚本0308的注释和输出结果。  

### EM算法
E 是期望的缩写，M 是最大的缩写，EM 算法是一种迭代优化策略。  
每轮迭代只要能够保证计算得到的概率值增大，且最终收敛即是有效。  
该算法适用于处理高斯混合模型问题，即包含多个高斯分布的复杂问题。  
参考脚本0309了解。

## 随机过程  
包括如下关键词和概念包括：蒙特卡罗方法、马尔可夫过程、高斯过程等。  
随机过程即一组有限或无限的随机变量序列，关注动态，建模场景包括：  
世界杯每场比赛进球数、沪深300指数每日收盘价、某路口每分钟车流量等。  

博彩场景，玩家和庄家对赌抛硬币分赌正反面，赌金1元，玩家本金10元。  
假设庄家本金无限，每个玩家最多赌100轮，输完全部本金则提前退出。  
参考脚本0401查看十个随机玩家100轮的对赌轮数和最终剩余本金数。  
再看0402可以了解随着赌博轮数的增加，更多的玩家会亏损和退出。  
即使不作弊只因为庄家的资金量是无穷的，玩得久了玩家就会输光破产。  

股票场景，金融工程中有如下的公式计算股价s在dt时间之后的新股价：  
s=s+mu*s*dt+sigma*s*e*sqrt(dt) 其中参数说明如下：  
* s - 目前股价
* mu - 股票收益率的期望值（可取0.15）
* sigma - 股票的波动率（可取0.2）
* dt - 估算期（一般取整年）/估算期间的交易次数（244个交易日）  
除了以上固定的参数值，只有e是一个服从标准正态分布的随机变量。  
参考脚本0403查看股价概率的分布情况模拟。  

上例考察最终股价，本例考察实时股价的随机变量序列，即随机过程展现。  
即不仅关注最终价格，而是记录每个步骤点的股票价格，参考脚本0404  
该价格路径呈现了蒙特卡罗方法的精髓，从宏观上直观展示了随机过程。  

### 到达过程
随机过程的种类繁多，主要有两种经典类型，即到达过程和马尔可夫过程。  
到达过程关注某种事件是否发成，如顾客到达时刻或车辆通过路口的时刻。  
到达过程又分服从几何分布的伯努利离散过程和指数分布的泊松连续过程。  
明显特征是相邻间隔事件独立，即上一个事件的结果不会影响下个事件。  

### 马尔可夫过程
与到达过程相对，马尔可夫过程的未来数据与历史数据存在关联，如股价。  
因为事件在时间上先后相关，所以马尔可夫过程也叫做马尔可夫链。  
根据时间是离散还是连续分布，马尔可夫链也分为离散和连续两种类型。  

离散时间的马尔可夫链有三个要素：离散时间、状态空间、和转移概率。  
状态空间即马尔可夫链在时刻 n 拥有的状态 Xn 所构成的集合 S  
转移概率即从状态 i 到状态 j 的转移发生的概率，举个例子如下：  
如果张三今天宅家，明天宅家觅食或运动的概率分别为0.2\0.6\0.2  
如果运动或觅食，如上概率分别为0.2\0.7\0.1和0.1\0.3\0.6  

马尔可夫特性：从时刻n的状态i转移到n+1时刻状态j的概率是一定的。    
即下一个状态Xn+1的概率分布只依赖于前一个状态Xn而与更早状态无关。  
pij即状态转移概率一定为正，且全状态空间的状态转移概率总和为一。  

所有状态的转移概率可用转移概率矩阵表示，仍以张三的次日活动为例：  
三个状态分别为：宅家 ｜ 运动 ｜ 觅食 - 得到如下概率转移矩阵  
0.2 0.2 0.6  
0.2 0.1 0.7  
0.1 0.3 0.6 即  
如果今天宅家，则明天宅家、运动或觅食的概率为0.2、0.2和0.6  
如果今天运动，则明天宅家、运动或觅食的概率为0.2、0.1和0.7  
如果今天觅食，则明天宅家、运动或觅食的概率为0.1、0.3和0.6  

### 多步转移
虽然每次转移的概率都只与当前状态有关，但也有多次转移的情景。  
比如社会流动性研究中有对贫穷、中产和富有状态之间转移概率的考察：  
0.7 0.2 0.1  
0.3 0.5 0.2  
0.2.0.4 0.4  
以上矩阵描述了贫穷、中产和富有到贫穷、中产和富有的转移概率。  
例如前辈中产，则后辈贫穷、中产或富有的概率为0.3、0.5和0.2  

因为世代连续，所以会有求祖辈贫穷父辈中产孙辈富有的概率的问题。  
这里分别将两步转移概率相乘即可，有：0.2 * 0.2 = 0.04  
如果只知道祖辈贫穷和孙辈富有，父辈状态未知即为隐状态，转移概率：  
0.7 * 0.1 + 0.2 * 0.2 + 0.1 * 0.4 = 0.15  
以上正好为矩阵第一行和第三列相乘，即矩阵二次幂后右上角的值。  
再复杂化，看脚本04056了解多父辈情况下的转移概率的收敛情况。  

### 进阶意义
观察多次迭代的马尔可夫链，可发现n步转移后的极限值与当前值无关。  
上例中，无论祖上状态如何n步转移后孙辈处于任何状态的概率都一样。  
这是因为三个状态之间可以互相转移，如果存在转移死角则极限不同。  
例如羊入虎口的场景，有四个状态：被吃、存活、存活、被吃和矩阵：  
  1   0   0   0  
0.2 0.4 0.4   0  
  0 0.4 0.4 0.2  
  0   0   0   1  
如果被吃就没有机会转移到其他状态，如存活则有0.4几率继续存活。  
存活时也有0.2几率被吃，其概率转移矩阵在n步后极限与初始值相关。 

参考脚本0407可以了解概率矩阵收敛于如下结果，且具有三个特性：  
  1   0   0   0  
0.6   0   0 0.4  
0.4   0   0 0.6  
  0   0   0   1  
第一和第四状态为吸收态，进入该状态就永远处于该状态，不会转移了。  
存在吸收态时n步转移收敛的极限值与初始状态有关，不同初始不同结果。  
随着n趋向无穷，生存概率收敛于0，即不论开始状态羊没有生存的希望。  

### 常返状态
如果一个状态可以转移入也可转移出，则为常返状态，否则为非常返。  
社会流动例子中三个状态都是常返，而羊入虎口例子中只有被吃是常返。  
这里如果有困惑，可以将常返理解为总是要掉入或无法逃出的意思。  

由常返状态构成的集合叫做常返类，一旦进入常返状态即永远停留其中。  
随着转移的继续，状态终将进入常返，可以将常返类看作一个大的吸收态。  

### 周期性
判断某个常返态是否存在周期性，可以看是否存在n值满足如下状态转移：  
至少存在一个特定状态，经过n步之后可以转移到常返类中的任何状态。  
如果存在如上条件的n则这个常返态就是非周期的，否则就是周期性的。  

### 稳态分析
稳态即不论初始状态如何，随着转移的继续，转移到其他状态的概率相同。  
马尔可夫链要收敛于一个稳态分布，必须是非周期且只含有一个常返类。  
在如上的一般条件上提出稳态分布的增强约束条件：不可约和正常返  

不可约即马尔可夫链中的任一状态在充分长时间转移后可以到达任意状态。  
即马尔可夫链中各状态之间全联通，稳态分布中每个状态的概率极限>0  

正常返即任一状态，从其他状态充分转移后首次到该状态的概率不为0  
该条件针对无限状态的马尔可夫链，保证稳态分布中每个状态概率都>0  

结论是，在不可约、非周期、正常返条件下：  
马尔可夫链有唯一稳态分布，且每个状态的概率都>0  

以社会流动性案为例，求解稳态概率[pi1, pi2, pi3]，有:  
                  ｜0.7 0.2 0.1｜  
[pi1, pi2, pi3] * ｜0.3 0.5 0.2｜ = [pi1, pi2, pi3]  
                  ｜0.2.0.4 0.4｜  
且 pi1 + pi2 + pi3 = 1

## 隐马尔可夫模型
Hidden Markov Model, HMM 是一种统计模型，广泛应用于自然语言处理。  
这里的隐是指最初的马尔可夫链是隐藏的，其生成的状态随机序列是可观测的。  

隐马尔可夫模型中所有隐状态构成状态集合Q，其中状态个数为N  
所有可能的观测结果构成的集合为V，观测到的结果个数为M  
经过一段时间T之后，生成长度为T的状态序列I，以及对应的观测序列O  

隐马尔可夫模型三要素：状态转移矩阵、观测概率矩阵、初始状态概率向量  
初始概率向量pi含有N个元素，即所有第一个状态的观测状态的概率。  
状态转移矩阵A是N个状态之间相互转移的概率，因此是一个NxN的方阵。  
观测概率矩阵B是N个状态在M次观测结果中出现的概率，是一个NxM的矩阵。  

齐次马尔可夫性：某时刻的隐状态只与前一时刻隐状态相关，与更早的无关。  
观测独立性：某时刻的观测结果只与该时刻的隐状态相关，与其他时刻无关。  

### 研究问题
隐马尔可夫模型可以研究哪些问题？  
一个是给定三要素的前提下，针对一个具体的观测序列，求它的出现概率。  
另一个是给定观测序列和三要素的前提下，求最可能对应的隐状态序列。  
这两个问题的范例参考脚本0408和0409的代码，注意代码实施需要更新。  

### 高斯过程
高斯过程的回归是一个先验+观测值-->后验的过程，其中涉及一个核心函数：  
径向基函数(Radial basis functions) - 参考脚本0410和0411了解  

## 统计推断
统计推断有精确推断和近似推断两种类型，后者又分确定性近似和随机近似。  
程序在建议分布上采样，对结果进行接受拒绝判断，等价实现目标分布采样。  
查看0501和0502了解采样目标和建议分布的比较及接受拒绝采样过程演示。  

选择一个与目标分布趋向一致的建议分布难度比较大，可结合马尔可夫链。  
回顾马尔可夫链的稳态定义，参考脚本0503代码和运行结果可直观了解。  

进入平稳状态后每个时刻的状态形成的样本集可以作为这个平稳分布的近似。  
进入平稳状态之前的时间叫做燃烧期，用大量样本和一个样本可得相同结果：  
即只对一个样本的一次转移做跟踪，用时间的平稳分布代替空间的平稳分布。  

参考脚本0504了解基于马尔可夫链的采样，注意其中燃烧期m参数的设置。  
其中生成随机状态的函数也很有趣，利用了转移概率的归一性，研究一下。  

### Metropolis-Hastings方法
第一步：随机选择一个起始点，指定燃烧期m和稳定期N。  
第二步：以上一轮采样值为均值和1为方差生成一个正态分布，随机取样。  
第三步：在[0,1]的均匀分布中随机生成一个数，并指定一个接收概率。  
如果随机生成数小于接收概率则接收新的采样值，否则仍然用旧的采样值。  

该方法美在其简洁，但如何计算接收概率和为什么可以如此计算是关键。  
具体可以检索改方法名了解方法背景和数学解释，参考脚本0505看模拟。  

### Gibbs采样方法
作为Metropolis-Hastings采样方法的一种特例，对高维分布进行采样。  
检索关键词了解方法和数学背景，参考脚本0506了解Gibbs采样的模拟。  