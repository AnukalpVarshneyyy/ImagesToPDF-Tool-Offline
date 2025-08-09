import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

# Set app theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class ImageToPDFApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image to PDF Converter")
        self.geometry("500x400")
        self.resizable(False, False)

        self.selected_images = []

        # Title Label
        title = ctk.CTkLabel(self, text="Image to PDF Converter", font=("Segoe UI", 24, "bold"))
        title.pack(pady=(40, 20))

        # Select Images Button
        self.select_btn = ctk.CTkButton(
            self,
            text="📁  Select Images",
            command=self.select_images,
            corner_radius=30,
            fg_color="#FF5C5C",
            hover_color="#FF3C3C",
            text_color="white",
            width=200,
            height=45
        )
        self.select_btn.pack(pady=10)

        # Info Label
        self.info_label = ctk.CTkLabel(self, text="No images selected", font=("Segoe UI", 14))
        self.info_label.pack(pady=10)

        # Convert Button
        self.convert_btn = ctk.CTkButton(
            self,
            text="📄  Convert to PDF",
            command=self.convert_to_pdf,
            corner_radius=30,
            fg_color="#4CAF50",
            hover_color="#43A047",
            text_color="white",
            width=200,
            height=45
        )
        self.convert_btn.pack(pady=20)

        # Footer credit
        credit_label = ctk.CTkLabel(
            self,
            text="Developed And Presented By Anukalp Varshney",
            font=("Segoe UI", 12, "italic"),
            text_color="#888888"
        )
        credit_label.pack(side="bottom", pady=10)

    def select_images(self):
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
        )
        self.selected_images = list(files)
        if self.selected_images:
            self.info_label.configure(text=f"{len(self.selected_images)} images selected ✅")
        else:
            self.info_label.configure(text="No images selected")

    def convert_to_pdf(self):
        if not self.selected_images:
            messagebox.showwarning("No Images", "Please select images first.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF File", "*.pdf")],
            title="Save PDF As"
        )

        if not save_path:
            return

        try:
            image_list = []
            for file in self.selected_images:
                img = Image.open(file).convert('RGB')
                image_list.append(img)

            image_list[0].save(save_path, save_all=True, append_images=image_list[1:])
            messagebox.showinfo("Success", f"PDF saved at:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert:\n{str(e)}")

if __name__ == "__main__":
    app = ImageToPDFApp()
    app.mainloop()
