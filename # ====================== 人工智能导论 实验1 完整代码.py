from sklearn.datasets import load_iris
iris = load_iris()
print(iris.DESCR)
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd
cancer = load_breast_cancer()
x = cancer.data
y = cancer.target
print(x[:5])
df = pd.DataFrame(x,columns=cancer.feature_names)
df['target']=y
print(df.head())
train_x,test_x,train_y,test_y=train_test_split(
    x,y,test_size=0.1,random_state=0
)
print("data:",x.shape)
print("target:",y.shape)
print("\n训练集样本数量:",train_x.shape[0])
print("\n测试集样本数量:",test_x.shape[0])

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target
train_x, test_x, train_y, test_y = train_test_split(
    x, y, test_size=0.1, random_state=0
)
model = DecisionTreeClassifier(random_state=0)
scores1 = cross_val_score(model, train_x, train_y, cv=5, scoring='accuracy')
print("训练集上的平均准确率: %0.2f (+/- %0.2f)" % (scores1.mean(), scores1.std() * 2))
model.fit(train_x, train_y)
pred2 = model.predict(test_x)
scores2 = accuracy_score(test_y, pred2)
print("在测试集上的准确率: %.2f" % scores2)
print("每次交叉验证的准确率: ")
print(scores1)
from sklearn.metrics import f1_score
y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]
f1 = f1_score(y_true, y_pred)
print(f"F1分数: {f1:.2f}")
import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
thresh = cm.max() / 2.

for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, format(cm[i, j], 'd'),
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black")
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()