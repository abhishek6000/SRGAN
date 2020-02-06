def generator():
  inputs = Input((256, 256, 3))
  x = Conv2D(64, (3, 3), padding='same', strides=1)(inputs)
  skip1 = PReLU()(x)

  x = Conv2D(64, (3, 3), padding='same', strides=1)(skip1)
  x = BatchNormalization()(x)
  x = PReLU()(x)
  x = Conv2D(64, (3, 3), padding='same', strides=1)(x)
  x = BatchNormalization()(x)
  skip2 = Add()([skip1, x])

  x = Conv2D(64, (3, 3), padding='same', strides=1)(skip2)
  x = BatchNormalization()(x)
  x = PReLU()(x)
  x = Conv2D(64, (3, 3), padding='same', strides=1)(x)
  x = BatchNormalization()(x)
  skip3 = Add()([skip2, x])

  x = Conv2D(64, (3, 3), padding='same', strides=1)(skip3)
  x = BatchNormalization()(x)
  x = PReLU()(x)
  x = Conv2D(64, (3, 3), padding='same', strides=1)(x)
  x = BatchNormalization()(x)
  skip4 = Add()([skip3, x])

  x = Conv2D(64, (3, 3), padding='same', strides=1)(skip4)
  x = BatchNormalization()(x)
  x = PReLU()(x)
  x = Conv2D(64, (3, 3), padding='same', strides=1)(x)
  x = BatchNormalization()(x)
  skip5 = Add()([skip4, x])

  x = Conv2D(64, (3, 3), padding='same', strides=1)(skip5)
  x = BatchNormalization()(x)
  x = PReLU()(x)
  x = Conv2D(64, (3, 3), padding='same', strides=1)(x)
  x = BatchNormalization()(x)
  skip6 = Add()([skip5, x])

  x = Conv2D(64, (3, 3), padding='same', strides=1) (skip6)
  x = BatchNormalization()(x)  
  x = Add()([skip1, x])
  x = Conv2D(256, (3, 3), padding='same', strides=1) (x)
  x = layers.UpSampling2D(3)(x)  #Check this
  x = PReLU()(x)
  x = Conv2D(256, (3, 3), padding='same', strides=1) (x)
  x = layers.UpSampling2D(3)(x)  #Check this
  x = PReLU()(x) 
  x = Conv2D(3, (9, 9), padding='same', strides=1) (x)

  model = Model(inputs=inputs, outputs=x)
  return model