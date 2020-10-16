import transformers


MAX_LEN = 512
TRAIN_BATCH_SIZE = 16
VALID_BATCH_SIZE = 2
EPOCHS = 15
# data and bert model path
BERT_PATH = "../input/"
MODEL_PATH = "model.bin"
TRAINING_FILE = "../input/data.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True
)
