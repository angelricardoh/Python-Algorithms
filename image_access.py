class ImageAccess:
    def __init__(self, channels, width, height):
        self.channels = channels
        self.width = width
        self.height = height
        self.value = [0] * (width * channels * height)

    def setPixel(self, x, y, value):
        for i in range(self.channels):
            self.value[(x * self.channels) + i + (y * self.width)] = value

    def accessPixel(self, x, y):
        result = [0] * self.channels
        for i in range(self.channels):
            result[i] = self.value[(x * self.channels) + i + (y * self.width)]
        return result

if __name__ == '__main__':
    testImage = ImageAccess(channels=3, width=224, height=224)
    testImage.setPixel(1, 2, 150)
    print(testImage.accessPixel(1, 2))
