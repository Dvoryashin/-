def dc(height, width):
    if height * 2 == width or width * 2 == height:
        return min(height, width)
    if height < width:
        while width - height > 0:
            width = width - height
        return dc(width, height)
    else:
        while height - width > 0:
            height = height - width
        return dc(height, width)
print(dc(50, 25))