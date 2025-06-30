import qrcode
import os

# Get URL and filename from the user
url = input("Enter the URL: ").strip()
filename = input("Enter the filename (without extension): ").strip()

# Check if URL was entered
if not url:
    print("Error: No URL entered.")
    exit()

# Set default filename if not provided
if not filename:
    filename = "default_qrcode"

# Create output directory if it doesn't exist
output_dir = "qrcodes"
os.makedirs(output_dir, exist_ok=True)

# Generate and save the QR code
output_path = f"{output_dir}/{filename}.png"
img = qrcode.make(url)
img.save(output_path)

print(f"QR code saved to: {output_path}")