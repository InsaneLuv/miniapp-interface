from graphql_query import Variable, Query, Field, Operation, Argument

operation = Operation(
    type='mutation',
    name='FetchWithdrawBet',
    variables=[
        Variable(name='order', type='Int!'),
    ],
    queries=[
        Query(
            name='withdraw_bet',
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
