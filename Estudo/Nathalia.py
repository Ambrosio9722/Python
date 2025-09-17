import numpy as np

import numpy as np
from skimage import util, color

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Gera uma imagem com 8 x 8 pixels e 8 níveis de intensidade
img_simple_rgb = np.random.randint(0, 8, size=(8, 8, 3), dtype=np.uint8)

# Imprime informações sobre a imagem
print(img_simple_rgb.shape, img_simple_rgb.dtype, img_simple_rgb.min(), img_simple_rgb.max())

# Plotando a imagem
plt.figure()
plt.imshow(img_simple_rgb / 7) # Converte para [0, ..., 1] para vizualização
plt.show()

# Calcula o histograma da imagem usando o NumPy
hist_simple_r, bins = np.histogram(img_simple_rgb[:,:,0], bins=8, range=(0, 7))
hist_simple_g, bins = np.histogram(img_simple_rgb[:,:,1], bins=8, range=(0, 7))
hist_simple_b, bins = np.histogram(img_simple_rgb[:,:,2], bins=8, range=(0, 7))

# Imprime os valores do histograma
print(hist_simple_r)
print(bins)

# Calcula o histograma normalizado da imagem usando o NumPy
hist_simple_r_norm = hist_simple_r / (img_simple_rgb.shape[0] * img_simple_rgb.shape[1])
hist_simple_g_norm = hist_simple_g / (img_simple_rgb.shape[0] * img_simple_rgb.shape[1])
hist_simple_b_norm = hist_simple_b / (img_simple_rgb.shape[0] * img_simple_rgb.shape[1])

# Imprime os valores do histograma
print(hist_simple_r_norm)
print(hist_simple_r_norm.sum())
print(bins)

fig, ((ax1, ax5, ax6), (ax2, ax3, ax4)) = plt.subplots(2,3, figsize=(9, 5))

# Plota o canal RED da imagem
im_0 = ax1.imshow(img_simple_rgb[:,:,0], cmap='Reds', vmin=0, vmax=7)
# Plota a barra de cores
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.05)
fig.colorbar(im_0, cax=cax)

# Plota o canal GREEN da imagem
im_1 = ax5.imshow(img_simple_rgb[:,:,1], cmap='Greens',  vmin=0, vmax=7)
# Plota a barra de cores
divider = make_axes_locatable(ax5)
cax = divider.append_axes("right", size="5%", pad=0.05)
fig.colorbar(im_1, cax=cax)

# Plota o canal BLUE da imagem
im_2 = ax6.imshow(img_simple_rgb[:,:,2], cmap='Blues',  vmin=0, vmax=7)
# Plota a barra de cores
divider = make_axes_locatable(ax6)
cax = divider.append_axes("right", size="5%", pad=0.05)
fig.colorbar(im_2, cax=cax)

# Plota o histograma (gráfico de barras) do canal RED da imagem
ch_0 = ax2.bar(np.arange(0, 8), hist_simple_r)
# *** Configurações do plot ***
ax2.autoscale(enable=True, axis='both', tight=True)
ax2.set_xticks(np.arange(0, 8, 2))
ax2.set_xticks(np.arange(0, 8, 1), minor=True)
ax2.set_yticks(np.arange(0, hist_simple_r.max()+0.01, 2), minor=False)
ax2.set_yticks(np.arange(0, hist_simple_r.max()+0.01, 1), minor=True)
ax2.grid(which='major', alpha=1.0)
ax2.grid(which='minor', alpha=0.5)
ax2.set_ylim(0, hist_simple_r.max()+1)
ax2.set_xlabel('Image intensities', fontsize='medium')
ax2.set_ylabel('Histogram', fontsize='medium')

# Plota o histograma (gráfico de barras) do canal GREEN da imagem
ch_1 = ax3.bar(np.arange(0, 8), hist_simple_g)
# *** Configurações do plot ***
ax3.autoscale(enable=True, axis='both', tight=True)
ax3.set_xticks(np.arange(0, 8, 2))
ax3.set_xticks(np.arange(0, 8, 1), minor=True)
ax3.set_yticks(np.arange(0, hist_simple_g.max()+0.01, 2), minor=False)
ax3.set_yticks(np.arange(0, hist_simple_g.max()+0.01, 2), minor=True)
ax3.grid(which='major', alpha=1.0)
ax3.grid(which='minor', alpha=0.5)
ax3.set_ylim(0, hist_simple_g.max()+1)
ax3.set_xlabel('Image intensities', fontsize='medium')
ax3.set_ylabel('Histogram', fontsize='medium')

# Plota o histograma (gráfico de barras) do canal BLUE da imagem
ch_2 = ax4.bar(np.arange(0, 8), hist_simple_b)
# *** Configurações do plot ***
ax4.autoscale(enable=True, axis='both', tight=True)
ax4.set_xticks(np.arange(0, 8, 2))
ax4.set_xticks(np.arange(0, 8, 1), minor=True)
ax4.set_yticks(np.arange(0, hist_simple_b.max()+0.1, 2), minor=False)
ax4.set_yticks(np.arange(0, hist_simple_b.max()+0.1, 1), minor=True)
ax4.grid(which='major', alpha=1.0)
ax4.grid(which='minor', alpha=0.5)
ax4.set_ylim(0, hist_simple_b.max()+1)
ax4.set_xlabel('Image intensities', fontsize='medium')
ax4.set_ylabel('Histogram', fontsize='medium')

fig.tight_layout()
plt.show()

# Carrega uma imagem do disco. Lembre-se de colocar no ambiente
#img_gray = plt.imread('boat.tif')
img_gray = plt.imread('carro.jpg')

print(img_gray.shape, img_gray.dtype, img_gray.min(), img_gray.max())

# Plotando a imagem
plt.figure()
plt.imshow(img_gray, cmap='gray')
plt.show()

# Calcula o histograma da imagem usando o NumPy
hist, bins = np.histogram(img_gray, bins=256, range=(0, 256))

fig = plt.figure()
plt.fill_between(bins[:-1], hist)

# Configurações do plot
plt.autoscale(enable=True, axis='both', tight=True)
ax = fig.gca()
ax.set_xticks(np.arange(0, 257, 32))
ax.set_xticks(np.arange(0, 257, 16), minor=True)
ax.set_yticks(np.arange(0, hist.max(), hist.max()//8), minor=False)
ax.set_yticks(np.arange(0, hist.max(), hist.max()//4), minor=True)

ax.grid(which='major', alpha=1.0)
ax.grid(which='minor', alpha=0.5)
ax.set_ylim(0, hist.max())
ax.set_xlabel('Intensidades da imagem', fontsize='medium')
ax.set_ylabel('Histograma', fontsize='medium')
plt.show()

hist_norm = hist / (img_gray.shape[0] * img_gray.shape[1])

fig = plt.figure()
# Using filled line plot
plt.fill_between(bins[:-1], hist_norm)

# Configurações do plot
plt.autoscale(enable=True, axis='both', tight=True)
ax = fig.gca()
ax.set_xticks(np.arange(0, 257, 32))
ax.set_xticks(np.arange(0, 257, 16), minor=True)
ax.set_yticks(np.arange(0, hist_norm.max()+0.01, hist_norm.max()/8), minor=False)
ax.set_yticks(np.arange(0, hist_norm.max()+0.01, hist_norm.max()/4), minor=True)
ax.grid(which='major', alpha=1.0)
ax.grid(which='minor', alpha=0.5)
ax.set_ylim(0, hist_norm.max())
ax.set_xlabel('Intensidades da imagem', fontsize='medium')
ax.set_ylabel('Histograma', fontsize='medium')
plt.show()

# Arranjo com os valores de intensidade possíveis em uma imagem de 8 bits sem sinal.
# [0, 1, 2, ..., 255]
r = np.linspace(0, 1, 256)

fig = plt.figure()
plt.plot(r, 1. - r)

#  Configurações do plot
plt.autoscale(enable=True, axis='both', tight=True)
ax = fig.gca()
ax.set_xticks(np.arange(0, 1.1, 0.2))
ax.set_xticks(np.arange(0, 1.1, 0.1), minor=True)
ax.set_yticks(np.arange(0, 1.1, 0.2), minor=False)
ax.set_yticks(np.arange(0, 1.1, 0.1), minor=True)
ax.set_aspect('equal')
ax.grid(which='major', alpha=1.0)
ax.grid(which='minor', alpha=0.5)
ax.set_ylim(0, 1)
ax.set_xlabel('Intensidade de entrada, $r$', fontsize='medium')
ax.set_ylabel('Intensidade de saída, $s$', fontsize='medium')

plt.show()

# Converte a imagem para float com valores no intervalo [0., 1.]
img_gray_float = util.img_as_float(img_gray)
img_gray_float2 = util.img_as_float(img_gray_2)

# Aplica a transformação negativa
img_neg = 1. - img_gray_float
img_neg2 = 1. - img_gray_float2

# Computa o histograma e o histograma normalizado da imagem original
hist, bins = np.histogram(img_gray_float2, bins=256, range=(0, 1))
hist_norm = hist / (img_gray_float2.shape[0] * img_gray_float2.shape[1])

# Computa o histograma e o histograma normalizado da imagem processada
hist_neg, bins_neg= np.histogram(img_neg2, bins=256, range=(0, 1))
hist_neg_norm = hist_neg / (img_neg2.shape[0] * img_neg2.shape[1])