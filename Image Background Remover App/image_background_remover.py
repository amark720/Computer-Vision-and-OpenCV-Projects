import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageFilter
from rembg import remove
import io


def remove_background():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )

    if not file_path:
        return  # Exit if no file is selected

    try:
        # Read and process the image
        with open(file_path, "rb") as f:
            input_image = f.read()
            output_image = remove(input_image, alpha_matting=True)

        # Load the image with background removed
        output_image = Image.open(io.BytesIO(output_image)).convert("RGBA")
        output_image = output_image.filter(ImageFilter.DETAIL)

        # Show the processed image
        show_image(output_image)
    except Exception as e:
        print(f"Error: {e}")


def show_image(image):
    # Display the image in a new window
    window = tk.Toplevel()
    window.title("Background Removed")
    window.geometry("1000x1000")

    # Resize image to fit within the window
    original_image = image
    image.thumbnail((800, 800))
    img_tk = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=img_tk)
    label.image = img_tk
    label.pack()

    # Save button to download the processed image
    save_button = tk.Button(
        window, text="Save Image", command=lambda: save_image(original_image)
    )
    save_button.pack()


def save_image(image):
    # Save the processed image
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG files", "*.png")]
    )
    if file_path:
        image.save(file_path)
        print(f"Image saved at: {file_path}")


# Main Application Window
root = tk.Tk()
root.title("Image Background Remover")
root.geometry("300x200")

# Add Buttons
upload_button = tk.Button(
    root, text="Upload Image", command=remove_background, width=20, height=2
)
upload_button.pack(pady=50)

root.mainloop()
