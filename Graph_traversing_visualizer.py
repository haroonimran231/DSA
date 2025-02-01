from tkinter import *
import time

class GraphTraversal:
    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(self.window, bg="chocolate", relief=RAISED, bd=7, width=500, height=600)
        self.make_canvas.pack()

        self.status = None
        self.vertex_store = []
        self.total_circle = []
        self.queue_bfs = []
        self.stack_dfs = []
        self.text_labels = []  # Store text labels inside circles

        self.basic_set_up()
        self.make_vertex()

    def basic_set_up(self):
        heading = Label(self.make_canvas, text="Graph Traversing Visualization", bg="chocolate", fg="yellow",
                        font=("Arial", 15, "bold", "italic"))
        heading.place(x=50, y=10)

        bfs_btn = Button(self.window, text="BFS", font=("Arial", 15, "bold"), bg="black", fg="green",
                         relief=RAISED, bd=8, command=self.bfs_traversing)
        bfs_btn.place(x=20, y=530)

        dfs_btn = Button(self.window, text="DFS", font=("Arial", 15, "bold"), bg="black", fg="green",
                         relief=RAISED, bd=8, command=self.dfs_traversing)
        dfs_btn.place(x=400, y=530)

        self.status = Label(self.make_canvas, text="Not Visited", bg="chocolate", fg="brown",
                            font=("Arial", 15, "bold", "italic"))
        self.status.place(x=50, y=550)

    def make_vertex(self):
        positions = [
            (220, 50),
            (180, 120), (260, 120),
            (140, 190), (220, 190), (300, 190),
            (100, 260), (180, 260), (260, 260), (340, 260),
            (60, 330), (140, 330), (220, 330), (300, 330), (380, 330)
        ]

        for i, (x, y) in enumerate(positions):
            oval = self.make_canvas.create_oval(x, y, x+30, y+30, width=3)
            text = self.make_canvas.create_text(x + 15, y + 15, text=str(i), font=("Arial", 12, "bold"), fill="white")
            self.total_circle.append(oval)
            self.text_labels.append(text)

        self.make_connector(0, 1)
        self.make_connector(0, 2)
        self.make_connector(1, 3)
        self.make_connector(1, 4)
        self.make_connector(2, 5)
        self.make_connector(3, 6)
        self.make_connector(3, 7)
        self.make_connector(4, 8)
        self.make_connector(5, 9)
        self.make_connector(6, 10)
        self.make_connector(7, 11)
        self.make_connector(8, 12)
        self.make_connector(9, 13)
        self.make_connector(9, 14)

    def make_connector(self, index1, index2):
        first_coord = self.make_canvas.coords(self.total_circle[index1])
        second_coord = self.make_canvas.coords(self.total_circle[index2])

        line_start_x = (first_coord[0] + first_coord[2]) / 2
        line_end_x = (second_coord[0] + second_coord[2]) / 2
        line_start_y = (first_coord[1] + first_coord[3]) / 2
        line_end_y = (second_coord[1] + second_coord[3]) / 2

        self.make_canvas.create_line(line_start_x, line_start_y + 10, line_end_x, line_end_y - 10, width=3)
        self.vertex_store.append((self.total_circle[index1], self.total_circle[index2]))

    def bfs_traversing(self):
        try:
            self.status['text'] = "Red: Visited"
            self.queue_bfs.append(self.vertex_store[0][0])
            visited = set()

            while self.queue_bfs:
                take_vertex = self.queue_bfs.pop(0)
                if take_vertex in visited:
                    continue
                visited.add(take_vertex)
                self.make_canvas.itemconfig(take_vertex, fill="red")
                self.window.update()
                time.sleep(0.3)

                for pair in self.vertex_store:
                    if pair[0] == take_vertex and pair[1] not in visited:
                        self.queue_bfs.append(pair[1])

            self.status['text'] = "All nodes Visited"
        except:
            print("Force stop error")

    def dfs_traversing(self):
        try:
            self.status['text'] = "Blue: Visited"
            self.stack_dfs.append(self.vertex_store[0][0])
            visited = set()

            while self.stack_dfs:
                take_vertex = self.stack_dfs.pop()
                if take_vertex in visited:
                    continue
                visited.add(take_vertex)
                self.make_canvas.itemconfig(take_vertex, fill="blue")
                self.window.update()
                time.sleep(0.3)

                for pair in self.vertex_store:
                    if pair[0] == take_vertex and pair[1] not in visited:
                        self.stack_dfs.append(pair[1])

            self.status['text'] = "All nodes Visited"
        except:
            print("Force stop error")

if __name__ == '__main__':
    window = Tk()
    window.title("Graph Traversal Visualizer")
    window.geometry("500x650")
    window.maxsize(500, 600)
    window.minsize(500, 600)
    window.config(bg="orange")
    GraphTraversal(window)
    window.mainloop()
