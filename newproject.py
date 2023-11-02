import qrcode

# Function to generate QR code
def generate_qr(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

# Example usage
data_to_encode = "https://mapari123.github.io/portfolio-/"  # Data you want to encode in the QR code
output_file = "qrcode_example.png"  # Output file name

generate_qr(data_to_encode, output_file)
print(f"A QR code has been generated with the data: {data_to_encode}.")



