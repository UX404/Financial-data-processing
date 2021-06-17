import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import time

#--------------------Load_Data--------------------
data_false = np.load('../data/data_false.npy')  # (59881, 16)
data_true = np.load('../data/data_true.npy')  # (446, 16)

#-------Data Processing: Copy/Merge/Shuffle-------
data_true_train = data_true[22:].repeat(134, axis=0)
data_true_test = data_true[:22].repeat(134, axis=0)  # 5% used as test set
data_false_train = data_false[2994:]
data_false_test = data_false[:2994]
data_train = np.concatenate((data_false_train, data_true_train), axis=0)
data_test = np.concatenate((data_false_test, data_true_test), axis=0)
np.random.shuffle(data_train)
np.random.shuffle(data_test)
x_train = data_train[:, :-1]
y_train = data_train[:, -1]
x_test = data_test[:, :-1]
y_test = data_test[:, -1]
print('Train data shape: ', x_train.shape, y_train.shape)
print('Test data shape: ', x_test.shape, y_test.shape)

#------------------Random_Forest------------------
print('Training...')
timer = time.time()
classifier = RandomForestClassifier(n_estimators=1000, bootstrap=True, max_samples=1000)
classifier.fit(x_train, y_train)
joblib.dump(classifier, 'random_forest.pkl')
print('Time for training:', time.time() - timer, 's')

#--------------------Evaluate---------------------
print('Evaluating...')
timer = time.time()
y_train_predict = classifier.predict(x_train)
y_test_predict = classifier.predict(x_test)
train_accuracy = metrics.accuracy_score(y_train, y_train_predict)
test_accuracy = metrics.accuracy_score(y_test, y_test_predict)
other_metrics = metrics.classification_report(y_test, y_test_predict)
print('Time for evaluation:', time.time() - timer, 's')
print('Training accuracy: %0.2f%%' % (train_accuracy*100))
print('Testing accuracy: %0.2f%%' % (test_accuracy*100))
print('Other metrics:', other_metrics)