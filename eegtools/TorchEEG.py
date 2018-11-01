import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torch.nn.functional as F
import torch.optim as optim

class TorchEEG(nn.Module):
    def __init__(self):
        super(TorchEEG, self).__init__()
