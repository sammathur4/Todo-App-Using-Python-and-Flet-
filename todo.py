from flet import *
from custom_checkbox import *


def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    PINK = '#eb06ff'

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(alignment='center',
                            controls=[
                                Container(padding=padding.all(5),
                                          bgcolor=BG,
                                          width=90, height=90,
                                          border_radius=50,
                                          content=Container(bgcolor=FG,
                                                            height=80, width=80,
                                                            border_radius=40,
                                                            content=CircleAvatar(opacity=0.8,
                                                                                 foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                                                                                 )
                                                            )
                                          )
                            ],
                            ),
            ),

        ]
    )

    def shirnk(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = \
            transform.Scale(0.8,
                            alignment=alignment.center_right)


        page_2.controls[0].border_radius = border_radius.only(
            topLeft=35,
            topRight=0,
            bottomLeft=35,
            bottomRight=0
        )
        page.update()


    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 25
        page_2.controls[0].scale = \
            transform.Scale(1,
                            alignment=alignment.center_right)

        page.update()


    """
    first_page_contents = Container(
    content=Column(
      controls=[
        Row(alignment='spaceBetween',
          controls=[
            Container(
              on_click=lambda e: shrink(e),
              content=Icon(
                icons.MENU)),
            Row(
              controls=[
                Icon(icons.SEARCH),
                Icon(icons.NOTIFICATIONS_OUTLINED)
              ],
            ),
          ],
        ),
        Container(height=20),
        Text(
          value='What\'s up, Olivia!'
        ),
        Text(
          value='CATEGORIES'
        ),
        Container(
          padding=padding.only(top=10,bottom=20,),
          content=categories_card
        ),
        Container(height=20),
        Text("TODAY'S TASKS"),
        Stack(
          controls=[
            tasks,
            FloatingActionButton(bottom=2,right=20,
              icon = icons.ADD,on_click=lambda _: page.go('/create_task')
            )
          ]
        )
      ],
    ),
  )
    
    """

    create_task_view = Container(
        content=Container(
            on_click=lambda _:page.go('/'),
            height=40,
            width=40,
            content=Text('x'))
    )




    tasks = Column(
        height=300,
        scroll='auto',
        # controls=[
        #     Container(height=50, width=300, bgcolor='red'),
        #     Container(height=50, width=300, bgcolor='red'),
        #     Container(height=50, width=300, bgcolor='red'),
        #     Container(height=50, width=300, bgcolor='red'),
        # ]
    )

    for i in range(10):
        tasks.controls.append(
            Container(height=70,
                      width=400,
                      bgcolor=BG,
                      border_radius=25,
                      padding=padding.only(left=20, top=20),
                      content=CustomCheckBox(
                          PINK,
                          size=20,
                          font_size=15,
                          label='Create Apps'
                      ),


                      )

        )

    categories_card = Row(
        scroll='auto'

    )
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                width=170,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=2 * i),
                            content=Container(
                                bgcolor=PINK,
                            )
                        )
                    ]
                )
            ),
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            on_click=lambda e:shirnk(e),
                            content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]

                        ),

                    ],
                    ),
                Container(height=20),
                Text(
                    value='What\'s up, Saksham'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20, ),
                    content=categories_card
                ),
                Text("Today's Task"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2, right=20,

                            icon=icons.ADD,
                            on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
        )
    )

    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=15,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[

                Row(alignment='start',
                    controls=[
                        Container(
                            border_radius=25,
                            height=50,
                            width = 50,
                            padding=padding.only(top=10,
                                                 left=3),
                            # border=border.all(color='white',
                            #                   width=1),
                            on_click= lambda e: restore(e),
                            content=Text('Back')
                        ),
                    ],
                ),

                Container(height=20),
                circle,
                Text("Saksham Mathur", size=15, weight='bold'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP),
                    Text("Templates", size=15, weight=FontWeight.W_300, color='white60', font_family='poppins'),
                ]),

                Row(controls=[
                    Icon(icons.CARD_TRAVEL),
                    Text("Templates", size=15, weight=FontWeight.W_300, color='white60', font_family='poppins'),
                ]),

                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED),
                    Text("Templates", size=15, weight=FontWeight.W_300, color='white60', font_family='poppins'),
                ]),

                # Graph Image
                Image(src = f"/images/1.png",
                      width=300,
                      height=200,),

                Text("Good", color=FG, font_family='poppins',),
                Text("Consistency", color=FG, font_family='poppins',),

            ]
        )
    )


    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents,
                    ]
                )

            )
        ]
    )

    container = Container(
        width=400,
        height=700,
        bgcolor=FWG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2,

            ]
        )
    )

    pages = {
        '/': View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ],
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container)

    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
