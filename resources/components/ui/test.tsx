import {
    Table,
    TableHeader,
    TableBody,
    TableHead,
    TableRow,
    TableCell,
} from "@/components/ui/table"

import React from "react"
import { fetchCargoListService } from "@/services/orders"

export function CargoShortTable() {
    const [data, setData] = React.useState<any[]>([])
    const [loading, setLoading] = React.useState(true)
    const [error, setError] = React.useState<string | null>(null)

    React.useEffect(() => {
        fetchCargoListService()
            .then((result) => {
                setData(result)
                setLoading(false)
            })
            .catch((e) => {
                setError(e.message)
                setLoading(false)
            })
    }, [])

    if (loading) return <div>Загрузка...</div>
    if (error) return <div>Не получилось загрузить данные. {error}</div>

    return (
        <div className="relative overflow-x-auto shadow-md sm:rounded-lg pb-32">
            {/* pb-32 — увеличенный отступ снизу, чтобы последнюю строку не перекрывал navbar */}
            <Table className="text-sm text-left text-gray-700">
                <TableHeader>
                    <TableRow className="uppercase bg-gray-50">
                        <TableHead className="px-3 py-2 whitespace-nowrap">№/Статус</TableHead>
                        <TableHead className="px-3 py-2 whitespace-nowrap">Маршрут</TableHead>
                        <TableHead className="px-3 py-2 whitespace-nowrap">Даты</TableHead>
                        <TableHead className="px-3 py-2 whitespace-nowrap">Груз</TableHead>
                        <TableHead className="px-3 py-2 whitespace-nowrap">Авто</TableHead>
                        <TableHead className="px-3 py-2 whitespace-nowrap">Стоимость</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {data.map((item, idx) => (
                        <TableRow key={item.id || idx} className="bg-white border-b hover:bg-gray-50">
                            <TableCell className="px-3 py-2 font-medium whitespace-nowrap">
                                <div className="flex flex-col gap-1">
                                    <button
                                        className="text-blue-600 hover:underline w-fit p-0 font-semibold"
                                        title="Открыть детали рейса"
                                    // onClick={() => ...} // сюда можно добавить обработчик клика
                                    >
                                        {item.id}
                                    </button>
                                    <div className="text-xs text-gray-500">{item.platform}</div>
                                    <div className="flex items-center gap-2 mt-1">
                                        {item.status ? (
                                            <span className="inline-block w-2 h-2 rounded-full bg-green-500" title="Активно" />
                                        ) : (
                                            <span className="inline-block w-2 h-2 rounded-full bg-gray-400" title="Не активно" />
                                        )}
                                    </div>
                                </div>
                            </TableCell>
                            <TableCell className="px-3 py-2 whitespace-nowrap">
                                <div className="flex flex-col gap-1">
                                    {item.route?.from && (
                                        <div>
                                            <span className="text-xs font-semibold mr-1">1.</span>
                                            <span className="font-semibold">{item.route.from}</span>
                                            <span className="text-xs text-gray-400 ml-1">{item.route.fromDesc}</span>
                                        </div>
                                    )}
                                    {item.route?.to && (
                                        <div>
                                            <span className="text-xs font-semibold mr-1">2.</span>
                                            <span className="font-semibold">{item.route.to}</span>
                                            <span className="text-xs text-gray-400 ml-1">{item.route.toDesc}</span>
                                        </div>
                                    )}
                                </div>
                            </TableCell>
                            <TableCell className="px-3 py-2 whitespace-nowrap">
                                <div>
                                    <div>
                                        <span className="font-semibold">Погрузка:</span> {item.loadingDate}
                                    </div>
                                    <div>
                                        <span className="font-semibold">Выгрузка:</span> {item.unloadingDate}
                                    </div>
                                </div>
                            </TableCell>
                            <TableCell className="px-3 py-2 whitespace-nowrap">
                                <div>
                                    <span>{item.cargo?.list?.join(", ")}</span>
                                    <div className="text-xs text-gray-400">
                                        {item.cargo?.weight} кг / {item.cargo?.pallet} паллет
                                    </div>
                                </div>
                            </TableCell>
                            <TableCell className="px-3 py-2 whitespace-nowrap">
                                <span>
                                    {item.veh?.type}, {item.veh?.tonnage}т
                                </span>
                            </TableCell>
                            <TableCell className="px-3 py-2 whitespace-nowrap">
                                <span className="font-bold">{item.cost}</span>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </div>
    )
}
