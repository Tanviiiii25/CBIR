import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Define image metadata with keywords
image_metadata = [
    # Add more images with keywords
    {"filename": "Beaches (1).jpg", "keywords": [" beach stall"]},
    {"filename": "Beaches (2).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (3).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (4).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (5).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (6).jpg", "keywords": ["beach", "sea", "beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (7).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (8).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (9).jpg", "keywords": ["beach", "sea","beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (10).jpg", "keywords": ["beach", "sea", "beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},
    {"filename": "Beaches (11).jpg", "keywords": ["beach", "sea", "beach", "ocean", "sand", "waves", "sun", "seashells", "seagulls", "palm trees", "swimming", "surfing", "relaxation", "vacation", "coastline", "shoreline", "tropical", "sunbathing", "beach volleyball", "sunset", "water sports"]},

    {"filename": "Bus (1).jpg", "keywords": ["bus","buses", "public transportation"]},
    {"filename": "Bus (2).jpg", "keywords": ["bus","buses", "   public transportation", "commute", "transport", "transit", "vehicle",  "school bus", ]},
    {"filename": "Bus (3).jpg", "keywords": ["bus","buses", "public transportation", "double decker bus" ]},
    {"filename": "Bus (103).jpg", "keywords": ["buses","bus", "double decker bus" ]},
    {"filename": "Bus (113).jpg", "keywords": ["buses" ,"bus","double decker bus"]},
    {"filename": "Bus (6).jpg", "keywords": [ "buses","bus","public transportation", "commute", "transport", "transit", "vehicle",  "travel", "bus stop", "passengers", "route", "fare", "bus driver", "bus terminal", "urban transport", "double decker bus", "bus station", "bus route", "bus timetable", "bus ticket"]},
    {"filename": "Bus (7).jpg", "keywords": ["buses","bus","public transportation", "commute", "transport", "transit", "vehicle",   "travel", "bus stop", "passengers", "route", "fare", "bus driver", "bus terminal", "urban transport", "double decker bus", "bus station", "bus route", "bus timetable", "bus ticket"]},
    {"filename": "Bus (8).jpg", "keywords": ["buses","bus", "public transportation", "commute", "transport", "transit", "vehicle", "city bus", "travel", "bus stop", "passengers", "route", "fare", "bus driver", "bus terminal", "urban transport", "bus station", "bus route", "bus timetable", "bus ticket"]},
    {"filename": "Bus (9).jpg", "keywords": ["buses","bus","public transportation", "commute", "transport", "transit", "vehicle",  "travel", "bus stop", "passengers", "route", "fare", "bus driver", "bus terminal", "urban transport", "double decker bus", "bus station", "bus route", "bus timetable", "bus ticket"]},
    {"filename": "Bus (10).jpg", "keywords": ["buses","bus","public transportation", "commute", "transport", "transit", "vehicle",   "travel", "bus stop", "passengers", "route", "fare", "bus driver", "bus terminal", "urban transport", "double decker bus", "bus station", "bus route", "bus timetable", "bus ticket"]},

    {"filename": "Flower (32).jpg", "keywords": ["flower", "yellow","yellow rose"]},
    {"filename": "Flower (9).jpg", "keywords": ["flower", "red","red rose"]},
    {"filename": "Flower (15).jpg", "keywords": ["flower", "red","red rose"]},
    {"filename": "Flower (99).jpg", "keywords": ["flower", "orange","orange rose"]},
    {"filename": "Flower (114).jpg", "keywords": ["flower", "white","white rose"]},
    {"filename": "Flower (144).jpg", "keywords": ["flower", "orange","orange rose"]},
    {"filename": "Flower (86).jpg", "keywords": ["flower", "pink","pink rose"]},
    {"filename": "Flower (199).jpg", "keywords": ["flower", "multicolor","multicolor rose"]},
    {"filename": "Flower (162).jpg", "keywords": ["flower", "red","red rose"]},
    {"filename": "Flower (187).jpg", "keywords": ["flower", "yellow"]},

    {"filename": "Elephants (21).jpg", "keywords": ["elephants", "animal", "animals"]},
    {"filename": "Elephants (22).jpg", "keywords": ["elephants", "animal", "animals"]},
    {"filename": "Elephants (23).jpg", "keywords": ["elephants", "animal", "animals"]},
    {"filename": "Elephants (24).jpg", "keywords": ["elephants", "mummy baby", "animal", "animals"]},
    {"filename": "Elephants (25).jpg", "keywords": ["elephants", "animal", "animals"]},
    {"filename": "Elephants (26).jpg", "keywords": ["elephants", "animal", "animals"]},
    {"filename": "Elephants (27).jpg", "keywords": ["elephants", "mummy baby", "animal", "animals"]},
    {"filename": "Elephants (28).jpg", "keywords": ["elephants", "mummy baby", "animal", "animals"]},
    {"filename": "Elephants (29).jpg", "keywords": ["elephants", "group", "animal", "animals"]},
    {"filename": "Elephants (30).jpg", "keywords": ["elephants", "group", "animal", "animals"]},

    {"filename": "Food (1).jpg", "keywords": ["foods","breads","bakery","fast food"]},
    {"filename": "Food (30).jpg", "keywords": ["foods","soup","fast food"]},
    {"filename": "Food (43).jpg", "keywords": ["foods","indian food","samosa"]},
    {"filename": "Food (258).jpg", "keywords": ["foods","fast food", "salsa"]},
    {"filename": "Food (248).jpg", "keywords": ["foods","fast food", "fries"]},
    {"filename": "Food (2).jpg", "keywords": ["foods","fast food","pizza"]},
    {"filename": "Food (271).jpg", "keywords": ["foods","salads","waffle"]},
    {"filename": "Food (57).jpg", "keywords": ["foods","salads","rice"]},
    {"filename": "Food (174).jpg", "keywords": ["foods","tacos","international","multicusine"]},
    {"filename": "Food (37).jpg", "keywords": ["foods","multicusine","pasta","international","multicusine","fast food"]},


    {"filename": "Fruit (3).jpeg", "keywords": ["red apple", "green apple", "yellow apple", "fruits"]},
    {"filename": "Fruit (9).jpeg", "keywords": ["red apple", "green apple", "yellow apple", "fruits"]},
    {"filename": "Fruit (17).jpeg", "keywords": ["red apple", "green apple", "yellow apple", "fruits"]},
    {"filename": "Fruit (67).jpeg", "keywords": ["yellow", "curved", "elongated","monkey food", "potassium symbol","fruits"]},
    {"filename": "Fruit (73).jpeg", "keywords": ["yellow", "curved", "elongated","monkey food", "potassium symbol","fruits"]},
    {"filename": "Fruit (93).jpeg", "keywords": ["yellow", "curved", "elongated","monkey food", "potassium symbol","fruits"]},
    {"filename": "Fruit (116).jpeg", "keywords": ["Grapevine", "Vineyard", "wine grapes","fruits"]},
    {"filename": "Fruit (120).jpeg", "keywords": ["Grapevine", "Vineyard", "wine grapes","fruits"]},
    {"filename": "Fruit (131).jpeg", "keywords": ["Grapevine", "Vineyard", "green grapes","fruits"]},
    {"filename": "Fruit (220).jpeg", "keywords": ["Tropical fruit", "Sweet", "raw mangoes", "mangoes", "fruits"]},
    {"filename": "Fruit (210).jpeg", "keywords": ["Tropical fruit", "Sweet", "mangoes", "fruits"]},
    {"filename": "Fruit (175).jpeg", "keywords": ["Tropical fruit", "Sweet", "mangoes", "fruits"]},
    {"filename": "Fruit (272).jpeg", "keywords": ["strawberry", "strawberries", "berry", "berries", "fruits"]},
    {"filename": "Fruit (275).jpeg", "keywords": ["strawberry", "strawberries", "berry", "berries", "fruits"]},
    {"filename": "Fruit (295).jpeg", "keywords": ["strawberry", "strawberries", "berry", "berries", "fruits"]},

    {"filename": "Tree (1).jpg", "keywords": ["trunk", "branches", "leaves", "roots","oak", "maple", "pine","tree" ]},
    {"filename": "Tree (2).jpg", "keywords": ["trunk", "branches", "leaves", "roots","oak", "maple", "pine","tree" ]},
    {"filename": "Tree (3).jpg", "keywords": ["trunk", "branches", "leaves", "roots","oak", "maple", "pine","tree" ]},
    {"filename": "Tree (4).jpg", "keywords": ["trunk", "branches", "leaves", "roots","oak", "maple", "pine" ,"tree"]},
    {"filename": "Tree (5).jpg", "keywords": ["trunk", "branches", "leaves", "roots", "oak", "maple", "pine","tree"]},
    {"filename": "Tree (6).jpg", "keywords": ["trunk", "branches", "leaves", "roots", "oak", "maple", "pine","tree"]},
    {"filename": "Tree (7).jpg", "keywords": ["trunk", "branches", "leaves", "roots", "oak", "maple", "pine","tree" ]},
    {"filename": "Tree (8).jpg", "keywords": ["trunk", "branches", "leaves", "roots", "oak", "maple", "pine","tree"]},
    {"filename": "Tree (9).jpg", "keywords": ["trunk", "branches", "leaves", "roots","oak", "maple", "pine","tree" ]},
    {"filename": "Tree (10).jpg", "keywords": ["trunk", "branches", "leaves", "roots", "oak", "maple", "pine","tree"]},

    {"filename": "Cars (1).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car" ,"Cars" ]},
    {"filename": "Cars (2).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "white car", "Cars"]},
    {"filename": "Cars (3).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car","Cars" ]},
    {"filename": "Cars (4).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "white car","Cars"]},
    {"filename": "Cars (5).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "blue car","Cars"]},
    {"filename": "Cars (6).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car","Cars"]},
    {"filename": "Cars (7).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car", "Cars"]},
    {"filename": "Cars (8).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car","Cars"]},
    {"filename": "Cars (9).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car","Cars" ]},
    {"filename": "Cars (10).jpg", "keywords": ["vehicle", "automobile", "transportation", "motor vehicle", "four-wheeled", "engine", "wheels", "driving", "red car","Cars"]},

    {"filename": "Aeroplane (1).jpg", "keywords": ["airplane", "aircraft", "flying machine", "blue plane", "aviation", "Aeroplane"]},
    {"filename": "Aeroplane (2).jpg", "keywords": ["airplane", "aircraft", "flying machine", "airbus plane", "aviation", "Aeroplane"]},
    {"filename": "Aeroplane (3).jpg", "keywords": ["airplane", "aircraft", "flying machine", "white plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (4).jpg", "keywords": ["airplane", "aircraft", "flying machine", "black plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (5).jpg", "keywords": ["airplane", "aircraft", "flying machine", "pacific plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (6).jpg", "keywords": ["airplane", "aircraft", "flying machine", "red plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (7).jpg", "keywords": ["airplane", "aircraft", "flying machine", "yellow plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (8).jpg", "keywords": ["airplane", "aircraft", "flying machine", "india plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (9).jpg", "keywords": ["airplane", "aircraft", "flying machine", "plane", "aviation","Aeroplane"]},
    {"filename": "Aeroplane (10).jpg", "keywords": ["airplane", "aircraft", "flying machine", "plane", "aviation","Aeroplane"]},

    {"filename": "Mountain & Snow (1).jpg", "keywords": ["mountain" "snow peak", "summit", ]},
    {"filename": "Mountain & Snow (2).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (3).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (4).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (5).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (6).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (7).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (8).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (9).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},
    {"filename": "Mountain & Snow (10).jpg", "keywords": ["mountain", "mountain range", "peak", "summit"]},

    {"filename": "Dinosaurs (10).png", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (11).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (12).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (13).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (14).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (15).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (16).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (17).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (18).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},
    {"filename": "Dinosaurs (19).jpg", "keywords": ["dinosaur", "dinosaurs", "Extinct"]},

    {"filename": "Bird (251).jpg", "keywords": ["bird", "parrot", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (295).jpg", "keywords": ["bird", "pigeon", "birds"]},
    {"filename": "Bird (77).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (78).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (101).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (138).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (142).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (241).jpg", "keywords": ["bird","birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (244).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},
    {"filename": "Bird (246).jpg", "keywords": ["bird", "birds", "colourful birds", "colourful bird"]},

    {"filename": "Peolpe_and_Villages_in_Africa (73).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (23).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (37).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (39).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (42).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (52).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (59).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (74).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (76).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},
    {"filename": "Peolpe_and_Villages_in_Africa (85).jpg", "keywords": ["african people", "african tribes", "african community", "africa", "african"]},

    {"filename": "Horses (33).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (34).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (35).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (36).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (37).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (38).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (39).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (40).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (41).jpg", "keywords": ["horses", "horse", "animal", "animals"]},
    {"filename": "Horses (42).jpg", "keywords": ["horses", "horse", "animal", "animals"]},

]

class TextBasedImageSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-Based Image Search")

        #self.background_image = Image.open("cbir.jpg")
        #self.background_image = self.background_image.resize((1530, 800))
        #self.background_image_tk = ImageTk.PhotoImage(self.background_image)
        #self.background_label = tk.Label(root, image=self.background_image_tk)
        #self.background_label.place(relwidth=1, relheight=1)

        self.query_label = tk.Label(root, text="Enter search keywords:")
        self.query_label.grid(row=0, column=0, columnspan=2, pady=50)

        self.query_entry = tk.Entry(root)
        self.query_entry.grid(row=0, column=2, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_images)
        self.search_button.grid(row=0, column=3, pady=10)

        self.results_frame = ttk.LabelFrame(root, text="Search Results")
        self.results_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.app_images = {}

        self.load_images()

    def load_images(self):
        for metadata in image_metadata:
            file_path = metadata["filename"]
            image = Image.open(file_path)
            image.thumbnail((350, 350))
            image_tk = ImageTk.PhotoImage(image)
            keywords = metadata.get("keywords", [])  # Use get to handle missing keywords
            self.app_images[file_path] = {"image": image, "image_tk": image_tk, "keywords": keywords}

    def search_images(self):
        query = self.query_entry.get().lower()

        if query:
            self.display_search_results(query)
        else:
            self.results_frame.grid_forget()
            tk.Label(self.root, text="Please enter keywords.").grid(row=2, column=0, columnspan=4, pady=10)


    def display_search_results(self, query):
        self.clear_results_frame()

        row, col = 0, 0
        images_per_row = 4
        for file_path, data in self.app_images.items():
            if any(keyword in query for keyword in data["keywords"]):
                image_label = tk.Label(self.results_frame, image=data["image_tk"])
                image_label.image = data["image_tk"]  # To prevent image from being garbage collected
                image_label.grid(row=row, column=col, padx=5, pady=5)



                col += 1
                if col >= images_per_row:
                    col = 0
                    row += 1

    def clear_results_frame(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TextBasedImageSearchApp(root)
    root.mainloop()