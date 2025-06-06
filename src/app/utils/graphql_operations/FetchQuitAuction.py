from graphql_query import Variable, Query, Field, Operation, Argument

operation = Operation(
    name='FetchQuitAuction',
    variables=[
        Variable(name='order', type='Int!'),
    ],
    queries=[
        Query(
            name='quit_auction',
            arguments=[
                Argument(name='order', value='$order'),
            ],
            fields=[
                Field(name='status'),
                Field(name='message'),
            ]
        )
    ]
)
