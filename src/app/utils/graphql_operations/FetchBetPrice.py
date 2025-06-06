from graphql_query import Variable, Query, Field, Operation, Argument

operation = Operation(
    name='FetchBetPrice',
    type='mutation',
    variables=[
        Variable(name='order', type='Int!'),
        Variable(name='price', type='Float!'),
        Variable(name='nds', type='Boolean'),
        Variable(name='comment', type='String'),
    ],
    queries=[
        Query(
            name='bet_price',
            arguments=[
                Argument(name='order', value='$order'),
                Argument(name='price', value='$price'),
                Argument(name='nds', value='$nds'),
                Argument(name='comment', value='$comment'),
            ],
            fields=[
                Field(name='status'),
                Field(name='message'),
            ]
        )
    ]
)
