import numpy as np

def getPixelMode(p1, p2, p3):
    return np.bitwise_or(np.bitwise_and(p3, np.bitwise_xor(p1, p2)), np.bitwise_and(p1, p2))

def getImageMode(img1, img2, img3):
    r, c = img1.shape[0], img1.shape[1]
    modal_image = np.zeros((r, c, 3), np.dtype('uint8'))
    for row in range(r):
        for col in range(c):
            p1, p2, p3 = img1[row, col, :], img2[row, col, :], img3[row, col, :]
            p = getPixelMode(p1, p2, p3)
            modal_image[row, col, :] = p
    return modal_image

def backgroundGeneration(V, L):
    resultArray = [np.zeros_like(V[0, :, :, :], np.dtype('uint8'))] * 3**(L-1)
    # Compute level 1 results
    for i in range(3**(L-1)):
        idxs = np.random.choice(len(V), 3)
        img1, img2, img3 = V[idxs[0], :, :, :], V[idxs[1], :, :, :], V[idxs[2], :, :, :]
        resultArray[i] = getImageMode(img1, img2, img3)
    
    # Compute results for higher levels
    for i in range(2, L):
        for j in range(3**(L-i)):
            img1, img2, img3 = resultArray[(3*j)], resultArray[(3*j)+1], resultArray[(3*j)+2]
            resultArray[j] = getImageMode(img1, img2, img3)
    return resultArray[0]


