def bilinear_resize(image, new_h, new_w):
    height, width = len(image), len(image[0])
    output = []
    for row in range(new_h):
        source_y = row * (height - 1) / (new_h - 1) if new_h > 1 else 0.0
        y0 = int(source_y)
        y1 = min(y0 + 1, height - 1)
        dy = source_y - y0
        output_row = []
        for column in range(new_w):
            source_x = column * (width - 1) / (new_w - 1) if new_w > 1 else 0.0
            x0 = int(source_x)
            x1 = min(x0 + 1, width - 1)
            dx = source_x - x0
            top = image[y0][x0] * (1 - dx) + image[y0][x1] * dx
            bottom = image[y1][x0] * (1 - dx) + image[y1][x1] * dx
            output_row.append(top * (1 - dy) + bottom * dy)
        output.append(output_row)
    return output
