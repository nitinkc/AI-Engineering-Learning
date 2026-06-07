# Hands-on Machine Learning Learning Guide: Neural Networks, CNNs, and Image Similarity Search

> **Audience:** Beginner who understands ML theory and wants hands-on coding practice.  
> **Main goal:** Move from basic neural networks to CNNs for images, and then prepare for an image similarity / visual search project.

---

## 1. What You Are Trying to Learn

You already have theory from Andrew Ng-style ML courses and from the attached visual search system document. The practical goal now is to learn how to write, train, test, and improve neural networks using real image datasets.

The learning path is:

```text
Basic ML workflow
    ↓
Basic neural network on image data
    ↓
CNN for images
    ↓
Pretrained CNN / ResNet
    ↓
Image embeddings
    ↓
Similarity search / visual search system
```

The attached document frames visual search as a ranking problem using representation learning: images are converted into embedding vectors, and visually similar images should be close to one another in embedding space.

---

## 2. Mental Model of Machine Learning

Every supervised ML project usually has these components:

```text
Data + Model + Loss Function + Optimizer + Training Loop + Evaluation = Trained ML System
```

### 2.1 Data

Data contains examples. For image classification:

```text
Input  = image
Output = label/class
```

Example:

```text
Input  = handwritten digit image
Output = 7
```

### 2.2 Model

A model is a function that maps input to output.

```text
model(image) → prediction
```

For classification, the output is usually a set of scores, one score per class.

### 2.3 Loss Function

A loss function measures how wrong the model is.

```text
loss = difference between prediction and true label
```

For multi-class classification, we commonly use:

```python
nn.CrossEntropyLoss()
```

### 2.4 Optimizer

The optimizer updates model weights to reduce loss.

Common optimizers:

- SGD
- Adam
- AdamW

For beginner projects, Adam is a good default:

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

### 2.5 Training Loop

A training loop repeatedly performs:

```text
1. Forward pass
2. Calculate loss
3. Backward pass
4. Update weights
```

---

## 3. Tools You Should Use

Recommended stack:

- Python
- PyTorch
- torchvision
- matplotlib
- scikit-learn, later
- FAISS, later for similarity search

Install basic packages:

```bash
pip install torch torchvision matplotlib
```

If using notebooks:

```bash
pip install notebook
```

---

## 4. Stage 1: Basic Neural Network on MNIST

### 4.1 Why MNIST?

MNIST is a classic beginner dataset of handwritten digits.

Each image is:

```text
1 x 28 x 28
```

Meaning:

```text
1  = grayscale channel
28 = height
28 = width
```

The label is one of:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

---

## 5. Basic Neural Network Code

### 5.1 Import Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
```

---

### 5.2 Prepare the Dataset

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)
```

### Explanation

`transforms.ToTensor()` converts an image into a PyTorch tensor.

`transforms.Normalize((0.5,), (0.5,))` normalizes pixel values so training becomes more stable.

`DataLoader` creates mini-batches.

Instead of training on one image at a time, we train on a batch:

```text
Batch size = 64
```

This means the model sees 64 images at once.

---

## 6. Define a Basic Neural Network

```python
class BasicNN(nn.Module):
    def __init__(self):
        super(BasicNN, self).__init__()

        self.flatten = nn.Flatten()

        self.network = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        x = self.network(x)
        return x
```

### 6.1 Shape Flow

Input image:

```text
1 x 28 x 28
```

Flattened:

```text
784
```

Network flow:

```text
784 → 128 → 64 → 10
```

The final 10 numbers are class scores.

Example:

```text
score for digit 0
score for digit 1
score for digit 2
...
score for digit 9
```

The class with the highest score becomes the prediction.

---

## 7. Create Model, Loss, and Optimizer

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = BasicNN().to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 7.1 Device

This line chooses GPU if available:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

### 7.2 Loss Function

Use cross entropy because this is multi-class classification.

```python
criterion = nn.CrossEntropyLoss()
```

### 7.3 Optimizer

Adam updates model weights.

```python
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

---

## 8. Training Loop

```python
num_epochs = 5

for epoch in range(num_epochs):
    model.train()

    running_loss = 0.0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    avg_loss = running_loss / len(train_loader)

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}")
```

### 8.1 Training Loop Breakdown

#### Step 1: Set model to training mode

```python
model.train()
```

#### Step 2: Move data to device

```python
images = images.to(device)
labels = labels.to(device)
```

#### Step 3: Clear old gradients

```python
optimizer.zero_grad()
```

#### Step 4: Forward pass

```python
outputs = model(images)
```

#### Step 5: Calculate loss

```python
loss = criterion(outputs, labels)
```

#### Step 6: Backpropagation

```python
loss.backward()
```

#### Step 7: Update weights

```python
optimizer.step()
```

---

## 9. Evaluate the Model

```python
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total

print(f"Test Accuracy: {accuracy:.2f}%")
```

### 9.1 Why `torch.no_grad()`?

During testing, we do not update weights. So we do not need gradients.

This saves memory and makes evaluation faster.

---

## 10. What You Should Learn From BasicNN

After running this, you should understand:

- how image data is loaded
- what a tensor is
- how a neural network is defined
- how forward pass works
- how loss is calculated
- how backpropagation updates weights
- how test accuracy is calculated

But there is one limitation:

```text
BasicNN flattens the image and loses spatial structure.
```

That is why CNNs are better for images.

---

# 11. Stage 2: CNN for Images

## 11.1 Why CNN?

A normal neural network sees the image as a long list of numbers:

```text
28 x 28 → 784
```

A CNN keeps the 2D structure:

```text
1 x 28 x 28
```

This helps the model learn visual patterns such as:

- edges
- corners
- curves
- strokes
- textures
- object parts

This is important because visual search systems often use CNN-based architectures such as ResNet to generate useful image representations.

---

## 12. Important CNN Concepts

### 12.1 Convolution Layer

A convolution layer applies filters to an image.

A filter is a small matrix that slides over the image and detects patterns.

Example:

```python
nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
```

Meaning:

```text
Input channels  = 1 grayscale channel
Output channels = 16 learned filters
Kernel size     = 3 x 3 filter
Padding         = keeps height/width same
```

### 12.2 ReLU Activation

```python
nn.ReLU()
```

ReLU adds non-linearity so the model can learn complex patterns.

### 12.3 Max Pooling

```python
nn.MaxPool2d(kernel_size=2)
```

Max pooling reduces spatial size.

Example:

```text
28 x 28 → 14 x 14
```

This reduces computation and keeps important features.

### 12.4 Fully Connected Layer

After convolution layers extract features, fully connected layers make final predictions.

---

# 13. Simple CNN Model for MNIST

```python
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()

        self.conv_layers = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),

            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x
```

---

## 14. CNN Shape Flow

Input:

```text
1 x 28 x 28
```

After first convolution:

```text
16 x 28 x 28
```

After first max pooling:

```text
16 x 14 x 14
```

After second convolution:

```text
32 x 14 x 14
```

After second max pooling:

```text
32 x 7 x 7
```

Flatten:

```text
32 * 7 * 7 = 1568
```

Final output:

```text
10 class scores
```

---

## 15. Train the CNN

Use the same training code as BasicNN. Only replace the model:

```python
model = SimpleCNN().to(device)
```

Keep the same loss and optimizer:

```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

Then run the same training loop.

---

## 16. Compare BasicNN vs CNN

After training both models, compare:

```text
BasicNN accuracy
CNN accuracy
```

You should usually see CNN perform better because it understands image structure better.

### Comparison Questions

Ask yourself:

1. Did CNN accuracy improve compared to BasicNN?
2. Did CNN loss reduce faster?
3. What happens if epochs increase from 5 to 10?
4. What happens if batch size changes from 64 to 128?
5. What happens if learning rate changes from 0.001 to 0.01?

---

# 17. Stage 3: CNN on CIFAR-10

After MNIST, move to CIFAR-10.

CIFAR-10 images are:

```text
3 x 32 x 32
```

Meaning:

```text
3  = RGB channels
32 = height
32 = width
```

Classes:

```text
airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
```

## 17.1 CIFAR-10 Dataset Code

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

train_dataset = datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.CIFAR10(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
```

## 17.2 CNN for CIFAR-10

```python
class CIFAR10CNN(nn.Module):
    def __init__(self):
        super(CIFAR10CNN, self).__init__()

        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x
```

### Shape Flow

Input:

```text
3 x 32 x 32
```

After pooling 1:

```text
32 x 16 x 16
```

After pooling 2:

```text
64 x 8 x 8
```

After pooling 3:

```text
128 x 4 x 4
```

Flatten:

```text
128 * 4 * 4 = 2048
```

Output:

```text
10 class scores
```

---

# 18. How This Connects to Image Similarity Search

Your attached visual search document explains that visual search can be framed as a ranking problem. Instead of predicting a class label, the system generates embeddings for images and ranks results based on similarity in embedding space.

Classification flow:

```text
Image → CNN → Class label
```

Similarity search flow:

```text
Image → CNN → Embedding vector → Similarity search → Ranked similar images
```

This is the bridge from CNN classification to visual search.

---

## 19. What Is an Embedding?

An embedding is a numeric vector representing an image.

Example:

```text
[0.12, -0.45, 0.88, ..., 0.03]
```

If two images are similar, their embeddings should be close.

This is the key idea behind visual search.

---

## 20. From CNN Classifier to Embedding Extractor

A trained CNN has two parts:

```text
Feature extractor + Classifier head
```

For image similarity, we often remove the final classification layer and use the feature vector before it.

Example concept:

```text
CNN layers → feature vector → classification layer
```

For similarity search:

```text
CNN layers → feature vector
```

The feature vector becomes the embedding.

---

## 21. Similarity Metrics

Common similarity/distance methods:

### 21.1 Cosine Similarity

Measures angle between vectors.

```python
import torch

similarity = torch.nn.functional.cosine_similarity(vec1, vec2, dim=0)
```

Higher cosine similarity means vectors are more similar.

### 21.2 Dot Product

```python
score = torch.dot(vec1, vec2)
```

### 21.3 Euclidean Distance

```python
distance = torch.norm(vec1 - vec2)
```

Lower distance means vectors are closer.

For high-dimensional embeddings, cosine similarity is often preferred.

---

# 22. Later Project: Simple Image Similarity Search

Once you complete CNN basics, build this project:

## Project Goal

Given a query image, return the top K visually similar images.

## Steps

```text
1. Load dataset
2. Train or use pretrained CNN
3. Extract embeddings for all images
4. Store embeddings
5. Select query image
6. Compute similarity between query and all images
7. Return top K most similar images
```

## Basic Pseudocode

```python
query_embedding = get_embedding(query_image)

scores = []

for image_id, embedding in database_embeddings:
    score = cosine_similarity(query_embedding, embedding)
    scores.append((image_id, score))

top_results = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
```

---

# 23. When to Use Which Algorithm

## 23.1 Logistic Regression

Use when:

- data is structured/tabular
- problem is simple
- interpretability matters

Example:

```text
Predict whether customer will churn based on age, income, usage
```

## 23.2 Decision Trees / Random Forests

Use when:

- tabular data
- non-linear relationships
- you want strong baseline performance

## 23.3 Neural Networks

Use when:

- data is unstructured
- data is large
- images, text, audio, video

## 23.4 CNNs

Use when:

- input is image-like
- spatial structure matters

Examples:

- image classification
- object detection
- visual search
- medical image analysis

## 23.5 Transformers / Vision Transformers

Use when:

- you have large datasets
- you want state-of-the-art vision models
- you can use pretrained models

## 23.6 Contrastive Learning

Use when:

- you care about similarity
- you want embeddings
- labels are limited
- you want representation learning

Examples:

- image similarity
- duplicate detection
- visual search
- face verification

## 23.7 Approximate Nearest Neighbor Search

Use when:

- you have many embeddings
- exact search is too slow
- you need fast retrieval

Common libraries:

- FAISS
- Annoy
- ScaNN

---

# 24. Common Errors and How to Debug

## 24.1 Shape Mismatch

Error example:

```text
mat1 and mat2 shapes cannot be multiplied
```

Cause:

```text
Your Linear layer input size does not match flattened tensor size.
```

Fix:

Print shape inside `forward`:

```python
def forward(self, x):
    x = self.conv_layers(x)
    print(x.shape)
    x = self.fc_layers(x)
    return x
```

## 24.2 Loss Not Decreasing

Possible reasons:

- learning rate too high
- learning rate too low
- model too small
- data not normalized
- labels incorrect

## 24.3 Accuracy Good on Train but Bad on Test

This is overfitting.

Solutions:

- use more data
- use data augmentation
- reduce model size
- use dropout
- use weight decay

## 24.4 Model Training Too Slowly

Possible fixes:

- use GPU
- reduce image size
- reduce model size
- increase batch size carefully

---

# 25. Practice Assignments

## Assignment 1: BasicNN on MNIST

Run the BasicNN model and record:

```text
Epoch 1 loss:
Epoch 2 loss:
Epoch 3 loss:
Epoch 4 loss:
Epoch 5 loss:
Test accuracy:
```

## Assignment 2: CNN on MNIST

Run SimpleCNN and record:

```text
Epoch 1 loss:
Epoch 2 loss:
Epoch 3 loss:
Epoch 4 loss:
Epoch 5 loss:
Test accuracy:
```

## Assignment 3: Compare Models

Answer:

```text
Which model performed better?
Why?
Did CNN train slower or faster?
Was the improvement worth it?
```

## Assignment 4: Change Hyperparameters

Try:

```text
batch_size = 32
batch_size = 128
learning_rate = 0.01
learning_rate = 0.0001
epochs = 10
```

Observe what changes.

## Assignment 5: Move to CIFAR-10

Train CIFAR10CNN and compare accuracy with MNIST results.

Expected observation:

```text
CIFAR-10 is harder than MNIST.
```

Why?

- color images
- more complex objects
- background noise
- object variation

---

# 26. Recommended Learning Schedule

## Week 1: PyTorch Basics

Focus:

- tensors
- datasets
- dataloaders
- simple neural network
- training loop

Deliverable:

```text
BasicNN trained on MNIST
```

## Week 2: CNN Basics

Focus:

- convolution
- pooling
- CNN architecture
- CNN training

Deliverable:

```text
SimpleCNN trained on MNIST
```

## Week 3: CIFAR-10

Focus:

- RGB images
- deeper CNN
- model debugging
- train/test comparison

Deliverable:

```text
CNN trained on CIFAR-10
```

## Week 4: Pretrained CNN

Focus:

- ResNet
- transfer learning
- feature extraction

Deliverable:

```text
Use pretrained ResNet as feature extractor
```

## Week 5: Image Embeddings

Focus:

- remove classification head
- extract embeddings
- cosine similarity

Deliverable:

```text
Generate embeddings for image dataset
```

## Week 6: Visual Search Mini Project

Focus:

- query image
- top K retrieval
- ranking
- visualization

Deliverable:

```text
Mini Pinterest-like image similarity search system
```

---

# 27. Final Big Picture

You are learning two connected ideas:

## Classification

```text
Image → Neural Network → Label
```

Example:

```text
Image of digit → 7
```

## Representation Learning / Similarity Search

```text
Image → Neural Network → Embedding → Similar images
```

Example:

```text
Image of dog → other visually similar dog images
```

Your attached visual search document focuses on the second idea. But to understand it properly, you first need hands-on practice with the first idea.

That is why the best order is:

```text
BasicNN → CNN → CIFAR-10 → ResNet → Embeddings → Similarity Search
```

---

# 28. Next Steps

After completing this guide, the next document/notebook should contain:

1. Complete runnable MNIST BasicNN notebook
2. Complete runnable MNIST CNN notebook
3. CIFAR-10 CNN notebook
4. Pretrained ResNet feature extraction notebook
5. Image similarity search notebook

Recommended next project:

```text
Build a simple image similarity search engine using CIFAR-10 and cosine similarity.
```

