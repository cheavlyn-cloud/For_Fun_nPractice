import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchtext.data.utils import get_tokenizer
import pygame

#define tensors
class TextDataSet(Dataset):
    def __init__(self, text, tokenizer, seq_length=30):
        self.tokenizer = tokenizer
        self.seq_length = seq_length

        #Tokenize the entire text into a list of words
        self.tokens = tokenizer(text)

        #Create i/o pairs, where Y is the next word
        self.data = []
        for i in range(len(self.tokens) - self.seq_length):
            X = self.tokens[i:i+self.seq_length]
            Y = self.tokens[i+self.seq_length]
            self.data.append((X, Y))
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        X, Y = self.data[idx]
        return torch.tensor(X), torch.tensor(Y)
    
#define Memory Model for laptop
class NeuralNetModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, seq_length):
        super(NeuralNetModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, vocab_size)
        self.seq_length = seq_length
    #embed network layers
    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        out = self.fc(lstm_out[:, -1, :])
        return out
    
def num_feed(file_path):
    num_string = ""
    try: 
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    num_string += line
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')
    # ASCII conversion
    ascii_codes = [num_string[i:i+3] for i in range(0, len(num_string), 3)]
    ascii_characters = [chr(int(code)) for code in ascii_codes]
    result = ''.join(ascii_characters)
    return result

# Now you can call it directly
input_nums = num_feed("your_file.txt")
    
input_nums = num_feed('')
#preprocess text
tokenizer = get_tokenizer('basic_english')
# Load or define your text
with open("your_file.txt", "r", encoding="utf-8") as f:
    book_text = f.read()
# Now create the dataset
dataset = TextDataSet(book_text, tokenizer, seq_length = 5)
#vocab to tokens
all_tokens = [token for sentence in dataset for token in sentence[0]]
vocab = set(all_tokens)
vocab_size = len(vocab)
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for idx, word in enumerate(vocab)}

#token to index
def tokens_to_indices(tokens):
    return [word_to_idx[token] for token in tokens]

#dataset to index only
class IndexedTextDataSet(TextDataSet):
    class IndexedTextDataSet(TextDataSet):
        def __getitem__(self, idx):
            X, Y = super().__getitem__(idx)
            # Convert X (list of tokens) into indices
            X_indices = tokens_to_indices(X)
            # Convert Y (a single token) into its index
            Y_index = word_to_idx[Y]
            return torch.tensor(X_indices), torch.tensor(Y_index)
    # Now you can create the dataset instance
    indexed_dataset = IndexedTextDataSet(book_text, tokenizer, seq_length=5)

#Create dataset instance
indexed_dataset = IndexedTextDataSet(book_text, tokenizer, seq_length=5)
#Create dataloader
batch_size = 2
data_loader = DataLoader(indexed_dataset, batch_size=batch_size, shuffle=True)
#Define model, loss, optimizer
embedding_dim = 10
hidden_dim = 50
model = NeuralNetModel(vocab_size, embedding_dim, hidden_dim, seq_length=5)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

#Training loop
epochs = 1000
for epoch in range(epochs):
    total_loss = 0
    for X, Y in data_loader:
        #pass forward
        optimizer.zero_grad()
        output = model(X)
        #calculate loss
        loss = criterion(output, Y)
        loss.backward()
        #update
        optimizer.step()
    print(f'Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(data_loader):.4f}')
def predict_next_word(input_sequence):
    model.eval()
    input_indices = torch.tensor(tokens_to_indices(input_sequence)).unsqueeze(0)
    with torch.no_grad():
        output = model(input_indices)
        _, predicted_idx = torch.max(output, dim = 1)
        total_loss += loss.item()
    return 
idx_to_word = {idx: word for idx, word in enumerate(vocab)}
input_sequence = input().split()
predicted_word = predict_next_word(input_sequence)
print(f'Input: {' '.join(input_sequence)}')
laptop_font = pygame.font.Font('Consolas.ttf', 20)
laptop_say = laptop_font.render(predicted_word, True, white = (255, 255, 255), black = (0, 0, 0))