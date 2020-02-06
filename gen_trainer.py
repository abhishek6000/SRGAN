def gen_trainer(low_batch,high_batch):
  g_pool = []   #Contains only 1 labels
  label_pool = []
  batch_size = 2    #Less than n
  for j in range(0,len(low_batch)):
    label_pool.append(1)