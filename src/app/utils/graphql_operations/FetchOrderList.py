from graphql_query import Variable, Query, Field, Operation, Argument

auction = Field(
    name='auction',
    fields=[
        Field(name='bets_count'),
        Field(name='end_date'),
        Field(name='current_date'),
        Field(name='bidding_disabled'),
        Field(name='step'),
        Field(name='ffa'),
        Field(name='start_gross_price'),
        Field(name='start_net_price'),
        Field(name='start_nds'),
        Field(name='type', fields=[
            Field(name='id'),
            Field(name='name'),
        ]),
        Field(name='members', fields=[
            Field(name='start_gross_price'),
            Field(name='start_net_price'),
            Field(name='start_nds'),
        ]),
        Field(name='bets', fields=[
            Field(name='id'),
            Field(name='carrier_company', fields=[
                Field(name='id'),
                Field(name='name'),
            ]),
            Field(name='gross_price'),
            Field(name='net_price'),
            Field(name='nds'),
            Field(name='comment'),
            Field(name='rank'),
        ]),
        Field(name='min_bet', fields=[
            Field(name='gross_price'),
            Field(name='net_price'),
        ]),
    ]
)

truck = Field(
    name='truck',
    fields=[
        Field(name='id'),
        Field(name='name')
    ]
)

client_company = Field(
    name='client_company',
    fields=[
        Field(name='id'),
        Field(name='name')
    ]
)


def depots(name):
    d = Field(
        name=name,
        fields=[
            Field(name='title'),
            Field(name='date_start'),
            Field(name='date_end'),
            Field(name='type'),
            Field(name='main'),
            Field(name='warehouse_id'),
            Field(name='warehouse', fields=[
                Field(name='transport_zone', fields=[
                    Field(name='code'),
                    Field(name='name'),
                ])
            ]),
            Field(name='location', fields=[
                Field(name='city'),
                Field(name='country'),
                Field(name='country_name'),
                Field(name='formatted'),
                Field(name='lat'),
                Field(name='lng'),
                Field(name='number'),
                Field(name='postal_code'),
                Field(name='region'),
                Field(name='street'),
            ]),
        ]
    )
    return d


operation = Operation(
    name='FetchOrderList',
    variables=[
        Variable(name='category', type='String'),
        Variable(name='perPage', type='Int'),
        Variable(name='page', type='Int'),
        Variable(name='sorting', type='String'),
        Variable(name='createdAtFrom', type='String'),
        Variable(name='createdAtTo', type='String'),
        Variable(name='loadingDateFrom', type='String'),
        Variable(name='loadingDateTo', type='String'),
        Variable(name='orderIds', type='[Int]'),
        Variable(name='internalIds', type='[String]'),
        Variable(name='countries', type='String'),
        Variable(name='regionIdsFrom', type='[String]'),
        Variable(name='regionIdsTo', type='[String]'),
        Variable(name='truckIds', type='[Int]'),
        Variable(name='clientCompanyId', type='Int'),
        Variable(name='betsExists', type='String'),
        Variable(name='transportZoneNameFrom', type='String'),
        Variable(name='transportZoneNameTo', type='String'),
        Variable(name='clientSecondLevelTypeIdsTo', type='[Int]'),
        Variable(name='carrierHasNewMessages', type='Boolean'),
    ],

    queries=[
        Query(
            name='order_list',
            arguments=[
                Argument(name='category', value='$category'),
                Argument(name='per_page', value='$perPage'),
                Argument(name='page', value='$page'),
                Argument(name='sorting', value='$sorting'),
                Argument(name='created_at_from', value='$createdAtFrom'),
                Argument(name='created_at_to', value='$createdAtTo'),
                Argument(name='loading_date_from', value='$loadingDateFrom'),
                Argument(name='loading_date_to', value='$loadingDateTo'),
                Argument(name='order_ids', value='$orderIds'),
                Argument(name='internal_ids', value='$internalIds'),
                Argument(name='countries', value='$countries'),
                Argument(name='region_ids_from', value='$regionIdsFrom'),
                Argument(name='region_ids_to', value='$regionIdsTo'),
                Argument(name='truck_ids', value='$truckIds'),
                Argument(name='client_company_id', value='$clientCompanyId'),
                Argument(name='bets_exists', value='$betsExists'),
                Argument(name='transport_zone_name_from', value='$transportZoneNameFrom'),
                Argument(name='transport_zone_name_to', value='$transportZoneNameTo'),
                Argument(name='client_second_level_type_ids_to', value='$clientSecondLevelTypeIdsTo'),
                Argument(name='carrier_has_new_messages', value='$carrierHasNewMessages'),

            ],
            fields=[
                Field(
                    name='data',
                    fields=[
                        Field(name='id'),
                        Field(name='created_at'),
                        Field(name='cargo_name'),
                        Field(name='category'),
                        Field(name='comment'),
                        Field(name='currency'),
                        Field(name='delivery_number'),
                        Field(name='distr'),
                        Field(name='status'),
                        Field(name='status_name'),
                        Field(name='edit_after_auction'),
                        Field(name='files'),
                        Field(name='guarantee'),
                        Field(name='has_new_chat_messages'),
                        Field(name='internal_id'),
                        Field(name='international'),
                        Field(name='new_chat_messages_count'),
                        Field(name='round_trip'),
                        Field(name='weight'),
                        Field(name='deleted_at'),
                        depots('loading_depots'),
                        depots('unloading_depots'),
                        auction,
                        client_company,
                        truck
                    ]
                ),
                Field(name='total'),
                Field(name='per_page'),
                Field(name='current_page'),
                Field(name='last_page'),

            ]
        )
    ]
)
