#9月17日尝试
#没有第一句代码报错pd没有定义
import pandas as pd
train_url ="d:\\train\\train.csv"
train = pd.read_csv(train_url)#括号内容多了个双引号即："train_url"报错FileNotFoundError: File b'train_url' does not exist找不到文件……
test ="d:\\test\\test.csv"
train["Pclass"].value_counts()
#了解并打印各个舱位都有多少乘客
print(train["Pclass"].value_counts())
train["Survived"].value_counts()
#了解乘客存活及丧生数量
print(train["Survived"].value_counts())
#统计幸存下来的男性与男性比率
print(train["Survived"][train["Sex"] == 'male'].value_counts())
#统计幸存下来的女性与女性比率
print(train["Survived"][train["Sex"] == 'female'].value_counts())
#调用布鲁萨德选取的算法
from sklearn import tree,preprocessing
#生成模型
target = train["Survived"].values
#预处理
encoded_sex =preprocessing .LabelEncoder()
#转换成数字
train.Sex = encoded_sex.fit_transform(train.Sex)
features_one = train[["Pclass", "Sex","Fare"]].values##报错：KeyError: "['Pclass,Sex,Age,Fare'] not in index"，KeyError字典关键字错误；
#not in index不是在指数；invalid character in identifier标识符中的无效字符.values后多了一个空格……
#9月18日找出原因，是因为“Ａge”的值有缺项。
#报错NotFittedError: This DecisionTreeClassifier instance is not fitted yet. Call 'fit' with appropriate arguments before using this method.
#这个决策器实例还没有安装。在使用此方法之前，请使用适当的参数调用“fit”。
#适合第一个决策树my_tree_one
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one,target)

print(my_tree_one.feature_importances_)

print(my_tree_one.score(features_one,target))
