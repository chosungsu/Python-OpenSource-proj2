# Keras: Deep Learning for humans

![Keras logo](https://s3.amazonaws.com/keras.io/img/keras-logo-2018-large-1200.png)

[![Build Status](https://travis-ci.org/keras-team/keras.svg?branch=master)](https://travis-ci.org/keras-team/keras)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/keras-team/keras/blob/master/LICENSE)

## You have just found Keras.

�ɶ󽺴� ���̽����� �ۼ��� ���� ������ �ΰ��Ű�� API �̸�, [TensorFlow](https://github.com/tensorflow/tensorflow), [CNTK](https://github.com/Microsoft/cntk), [Theano](https://github.com/Theano/Theano)���� ���� ���� �� �� �ֽ��ϴ�. �̷��� ���� ���� ������ �����ϰ� ����� ���� �������� ��� ���ߵǾ����ϴ�. ���� ������ �س��� �뿡 �־� ���� �߿��� ���� ������ ���� �ð����� ���̵��� ����� ���� �س��� ���� �����ϰ� ����� ���Դϴ�.
�Ʒ��� ���� ����� ���� ������ ���̺귯���� �ʿ�� �Ѵٸ� �ɶ󽺸� ����Ͻʽÿ�.

* ���� ģ����, ��⼺, Ȯ�强�� ���Ͽ� ���� ���� ������ Ÿ������ �����ϵ��� ���ݴϴ�. 
* �ռ��� �Ű��(Convolutional network) �� �����ϴ� ��Ʈ��ũ�� ������ �Ӹ� �ƴ϶�, �� ���� ���� ���� ���� �����մϴ�.
*CPU �� GPU���� �Ϻ��ϰ� �����˴ϴ�.

�ڼ��� ������ [Keras.io](https://keras.io).���� �����Ͻʽÿ�.
�ɶ󽺴� __Python 2.7-3.6__ �� ȣȯ�˴ϴ�.

------------------


## Guiding principles


- **����ģ����** �ɶ󽺴� ��谡 �ƴ� ����� ���� �����ε� API �Դϴ�. �̷��� Ư¡�� ������ �ֿ켱 ���� �߽����� �����մϴ�. �ɶ󽺴� �������� �δ��� ���̴µ��� �־� ������ ���� �ּ��� ������ �����մϴ� : �ɶ󽺴� �ϰ����̰� ������ API�� �����ϸ�, ����ϰ� ����ϴ� ���� �־� �ʿ��� ������ �ൿ�� �ּ������� ���̰�, ������ ������ ���� ��Ȯ�ϰ� Ȱ������ �ǵ���� �����մϴ�.

- **��⼺** �� ���� ������ ���� �������� �����, ������ ���� ������ ����� ���� ������ �׷��� Ȥ�� ������ �� �޾Ƶ鿩���� �ֽ��ϴ�. Ư����, neural layers, cost functions, optimizers, initialization schemes, activation functions and regularization schemes ���� ��� ���ο� �𵨰� ���յ� �� �ִ� ���� ������ ���� �Դϴ�.

- **���� Ȯ�强** ���ο� ������ ���ο� Ŭ������ ������ν� �߰��ϱ� �����, �����ϴ� ������ ����� ������ �������ݴϴ�. ���ο� ��� ����⸦ ���� �ϴ� ���� �ɶ󽺸� ��ȭ�� ������ �����ϰ� ����� ������ ǥ������ �����մϴ�.

- **���̽�� �Բ� �۵�** ������ ������ �и��� �� ���� ������ �������� �ʽ��ϴ�. ���� �����ϰ�, ����� �ϱ� ����� Ȯ���� �������� �����ϴ� ���̽� �ڵ�� ǥ�õǾ� �ֽ��ϴ�. 

------------------


## Getting started: 30 seconds to Keras
�ɶ��� �߿� ������ ������ ���̾ �����ϴ� ����� �� �Դϴ�. ���� ������ Ÿ���� ���� ���� ���� ������ ���̾ ���� ������ ���Դϴ�.  �� ������ ������ ���ؼ��� ������ �׷����� ���̾ ���� �� �ֵ��� ���ִ� �ɶ��� ����� API�� ����ؾ߸� �մϴ�.

���� ������ ���� �ֽ��ϴ�.

```python
from keras.models import Sequential

model = Sequential()
```

���� ���̾�� .add() ��ŭ�̳� �����ϴ�.

```python
from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
```

����� ���� ������ ���δٸ�, compile() �� ���� Ȯ���� ���ʽÿ�.

```python
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

�ʿ�θ� �Ѵٸ�, ����� optimizer �� ���� �� ��� Ȯ���� �� �� �ֽ��ϴ�. �ɶ��� �ٽ����� ��Ҵ� ������ �ʿ�� �� �� ������ ���� ��Ʈ�� �� �� �ֵ��� �ϸ� ���� �͵��� �ո������� �����ϰ� ����� ���Դϴ�. 

```python
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
```

����� ���� ����� ������ �������� �ϰ� ó���� �ݺ��� �� �ֽ��ϴ�.

```python
# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
model.fit(x_train, y_train, epochs=5, batch_size=32)
```

���ÿ�, ����� ����� �𵨿� �ϰ�ó���� ���������� ������ �� �ֽ��ϴ�.

```python
model.train_on_batch(x_batch, y_batch)
```

����� �������� �� �ٷ� ���Ͻʽÿ�.

```python
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
```

�Ǵ� ���ο� �����Ϳ� ���� ���󵵸� ���� ���ʽÿ�.

```python
classes = model.predict(x_test, batch_size=128)
```

�ý����̳� �̹��� �з� ��, Neural Turing Machine �̳� �ٸ� �𵨿� ���ϸ� ������ ������ ���� ����� �����ϴ�. �������� �ڿ� �����ִ� ���̵��� �����ѵ�, �װ͵��� �����ϴ� ������ ��ٷο��߸� �ұ��?

�ɶ��� ���丮�� ���� �� ���� �İ��� �ʹٸ�, �� ���� ������ ���ʽÿ�

- [Getting started with the Sequential model](https://keras.io/getting-started/sequential-model-guide)
- [Getting started with the functional API](https://keras.io/getting-started/functional-api-guide)


�������丮�� ���� ���� �ȿ���, ���� LSTMS�� �̿��� �ؽ�Ʈ ������, �޸� ��Ʈ��ũ�� �̿��� ���� ���� ��� �� �� ���� ��ȭ�� �𵨵��� �ֽ��ϴ�.

------------------


## Installation

�ɶ󽺸� ��ġ�ϱ� ������, TensorFlow, Theano, CNTK �� �ϳ��� �⺻ �������μ� ��ġ���ֽñ� �ٶ��ϴ�. (TensorFlow��õ)

- [TensorFlow installation instructions](https://www.tensorflow.org/install/).
- [Theano installation instructions](http://deeplearning.net/software/theano/install.html#install).
- [CNTK installation instructions](https://docs.microsoft.com/en-us/cognitive-toolkit/setup-cntk-on-your-machine).

���� ���û��׵��� ��ġ�ϴ� �͵� ����Ͻñ� �ٸ��ϴ�.

- [cuDNN](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/) (GPU���� �ɶ󽺸� ���� �����̶�� ��õ).
- HDF5 and [h5py](http://docs.h5py.org/en/latest/build.html) (��ũ�� �ɶ� ���� ������ �����̶�� �ʼ�).
- [graphviz](https://graphviz.gitlab.io/download/) and [pydot](https://github.com/erocarrera/pydot) (�� �׷����� ������ ���� [visualization utilities](https://keras.io/visualization/) �� ���� ����).

�׸�����, �ɶ󽺸� ���������� ��ġ�Ͻʽÿ�. �ɶ󽺸� ��ġ�ϴ� ���� �ΰ��� ����� �ֽ��ϴ�.


- **�ɶ󽺸� PyPl�κ��� ��ġ�ϱ� (��õ)**


�� ��ġ ����� �������� �� ȯ�濡 ģȭ�Ǿ� �����Ƿ�, ������ ȯ�濡�� �����ϱ� ���Ѵٸ� �Ʒ� �ڵ忡�� sudo �κ��� �����ؾ߸� �մϴ�.

```sh
sudo pip install keras
```

����ȯ���� ����ϰ� �ִٸ�, sudo ����� ��ġ ���� ���� �ֽ��ϴ�.

```sh
pip install keras
```

- **��ü ���:  �ɶ󽺸� GitHub�� �ҽ��� �̿��� ��ġ�ϱ�**

ù��°��, git�� ����Ͽ� Keras�� clone�Ͻʽÿ�.

```sh
git clone https://github.com/keras-team/keras.git
```

�׸�����, �ɶ� ������ cd�� �Է��� �� ��ġ ����� �����Ͻʽÿ�.

```sh
cd keras
sudo python setup.py install
```

------------------


## Configuring your Keras backend

�⺻������, �ɶ󽺴� tensor ���� ���̺귯���ν� �ټ��÷ξ ����� ���Դϴ�. �ɶ��� �鿣�带 �����ϰ� �ʹٸ� [�� ����](https://keras.io/backend/)�� �����ֽʽÿ�.

------------------


## Support


������ �� ���� �ְ� ���� ��п� ������ ���� �ֽ��ϴ�.

*[�ɶ� ���� �׷�](https://groups.google.com/forum/#!forum/keras-users)
*[�ɶ� Slack channel ](https://kerasteam.slack.com)�� �̿��ϰ� �����ôٸ� �� [��ũ](https://keras-slack-autojoin.herokuapp.com/)�� ����� ��û���� ��û�Ͻʽÿ�.
���� **���� �Ű� ���� ��û**�� Github issues������ �ٷ� �� �ֽ��ϴ�. [���̵����](https://github.com/keras-team/keras/blob/master/CONTRIBUTING.md)�� �����Ͽ� �ֽʽÿ�.

------------------


## Why this name, Keras?

�ɶ󽺴� �׸������ ���� �ǹ��մϴ�. �̷��� ���� ���� ��ȥ���� �ΰ����� ������ ȯ������ ���̰�, ����ǰ����� ���� ������ �����Ͽ�����, ������ �����ϰ� �� �̷��� �˸���, ���� ������ ���� ������ �̵鿡 ���� �������� �����̿��� ó������ �߰ߵ� ��� �׸����� ��ƾ�� ��ȭ�κ��� ������� ������ �̹����� �����ϰ� �ֽ��ϴ�. ���� �͵��� ��� �԰� ����, �׸��� ��ƿ� ���� ���� �ܾ���� �����Դϴ�.
�ɶ󽺴� �ʹݿ� ONEIROS ������Ʈ�� ������ ��ȯ���μ� ���ߵǾ����ϴ�. (Open-ended Neuro-Electronic Intelligent Robot Operating System).

>_"Oneiroi are beyond our unravelling --who can be sure what tale they tell? Not all that men look for comes to pass. Two gates there are that give passage to fleeting Oneiroi; one is made of horn, one of ivory. The Oneiroi that pass through sawn ivory are deceitful, bearing a message that will not be fulfilled; those that come out through polished horn have truth behind them, to be accomplished for men who see them."_ Homer, Odyssey 19. 562 ff (Shewring translation).

------------------