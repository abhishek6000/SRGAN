def discriminator():
  inputs1 = Input(shape=(256, 256, 3))
  
  b = Conv2D(64, (3, 3), padding='same', strides=1)(inputs1)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(6, (3, 3), padding='same', strides=2)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(128, (3, 3), padding='same', strides=1)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(128, (3, 3), padding='same', strides=2)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(256, (3, 3), padding='same', strides=1)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(256, (3, 3), padding='same', strides=2)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(512, (3, 3), padding='same', strides=1)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Conv2D(512, (3, 3), padding='same', strides=2)(b)
  b = BatchNormalization()(b)
  b = LeakyReLU(alpha=0.1)(b)

  b = Dense(1024)(b)
  b = LeakyReLU(alpha=0.1)(b)
  b = Dense(1,activation='sigmoid')(b)

  model2 = Model(inputs=inputs1, outputs=b)
  return model2