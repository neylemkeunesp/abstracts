import torch
from torch.nn.functional import softmax
from torchvision import transforms
from torchvision import models
from torch.nn.utils.rnn import pack_padded_sequence
from nltk.translate.meteor_score import meteor_score
import cv2
import matplotlib.pyplot as plt

#Load pre-trained SAT model
model = models.resnet152()
model.eval()

# Preprocess image
img = cv2.imread("/Users/neylemke/Downloads/grid_0.png")

# Preprocess image
img = cv2.imread("/Users/neylemke/Downloads/grid_0.png")

img = cv2.resize(img, (224,224))
plt.imshow(img)
img = img.transpose(2, 0, 1)
transform = transforms.Compose([
transforms.ToTensor(),
transforms.Resize(256),
transforms.CenterCrop(size=224),
#transforms.Normalize(mean = [0.485, 0.456, 0.406],
#std = [0.229, 0.224, 0.225])
transforms.Normalize,
]
)
img2 = transform(img)

# Forward pass image through the model
output = model(img2.unsqueeze(0))
output = softmax(output, dim=1)


