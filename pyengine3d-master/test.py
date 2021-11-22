import graphics.engine

test = graphics.engine.Engine3D([[1, 1, 1], [0, 0, 0], [2, 2, 2]], [[0, 1, 2]]) # this will create a single triangle between these points
test.writePoints([[3, 3, 3], [0, 0, 0], [2, 2, 2]]) # change the points
test.clear()
test.render()
test.screen.window.mainloop()