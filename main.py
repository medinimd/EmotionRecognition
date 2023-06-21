import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import streamlit as st
import tensorflow as tf
import streamlit as st


def load_model():
  model=tf.keras.models.load_model('my_model2.hdf5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

streamlit run [main.py]
