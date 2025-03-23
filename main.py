import flet as ft

def main(page: ft.Page):
    page.title = "Flet Drawer Example"

    # Function to open the drawer
    def open_drawer(e):
        page.drawer.open = True
        page.update()

    # Function to set the drawer width dynamically
    def set_drawer_width(e):
        page.drawer.width = page.width * 0.75  # 3/4 of the available width
        page.update()

    # Create a drawer
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Text("Drawer Content", size=20, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Option 1"),
            ft.Text("Option 2"),
            ft.Text("Option 3"),
        ]
    )

    # Ensure the drawer resizes dynamically
    page.on_resize = set_drawer_width

    # Button to trigger the drawer
    btn_open_drawer = ft.ElevatedButton("Open Drawer", on_click=open_drawer)

    page.add(btn_open_drawer)

ft.app(target=main)
