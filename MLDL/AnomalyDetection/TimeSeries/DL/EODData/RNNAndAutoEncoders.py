import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load and preprocess your two-dimensional time series dataset
# Assuming your dataset is in a pandas DataFrame with columns 'date' and 'value'
data = pd.read_csv('your_dataset.csv')
dates = pd.to_datetime(data['date'])
values = data['value']

# Normalize the values
normalized_values = (values - np.mean(values)) / np.std(values)

# Prepare input sequences for the RNN
sequence_length = 10  # Number of previous time steps to consider for each data point
input_sequences = []
for i in range(sequence_length, len(normalized_values)):
    input_sequences.append(normalized_values[i - sequence_length: i + 1])
input_sequences = np.array(input_sequences)

# Split the data into training and validation sets
train_ratio = 0.8
train_size = int(train_ratio * len(input_sequences))
train_data = input_sequences[:train_size]
val_data = input_sequences[train_size:]

# Define the RNN-Autoencoder model
latent_dim = 10

# Encoder
encoder_inputs = keras.Input(shape=(sequence_length + 1,))
encoder = layers.LSTM(latent_dim, return_sequences=False)(encoder_inputs)

# Decoder
decoder_outputs = layers.RepeatVector(sequence_length + 1)(encoder)
decoder_outputs = layers.LSTM(latent_dim, return_sequences=True)(decoder_outputs)
decoder_outputs = layers.TimeDistributed(layers.Dense(1))(decoder_outputs)

# Define the RNN-Autoencoder model
model = keras.Model(encoder_inputs, decoder_outputs)

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Train the model
model.fit(train_data, train_data, validation_data=(val_data, val_data), epochs=50, batch_size=16)

# Reconstruct the training data using the trained model
reconstructed_train_data = model.predict(train_data)

# Calculate reconstruction error (MSE) between original and reconstructed data
train_mse = np.mean(np.power(train_data - reconstructed_train_data, 2), axis=1)

# Set a threshold for anomaly detection
threshold = 0.1  # Adjust the threshold based on your dataset and requirements

# Identify anomalies in the training data
train_anomalies = dates[sequence_length:train_size][train_mse > threshold]

# Print the detected anomalies in the training data
print("Detected anomalies in the training data:")
print(train_anomalies)

# Reconstruct the validation data using the trained model
reconstructed_val_data = model.predict(val_data)

# Calculate reconstruction error (MSE) between original and reconstructed data
val_mse = np.mean(np.power(val_data - reconstructed_val_data, 2), axis=1)

# Identify anomalies in the validation data
val_anomalies = dates[train_size + sequence_length:][val_mse > threshold]

# Print the detected anomalies in the validation data
print("Detected anomalies in the validation data:")
print(val_anomalies)