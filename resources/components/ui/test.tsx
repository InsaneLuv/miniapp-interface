import React from "react"
import { fetchCargoListService } from "@/services/orders"
import { API } from "@/types/api"

export function CargoShortTable() {
  const [data, setData] = React.useState<API.CargoList.ResponseBody>([])
  const [loading, setLoading] = React.useState(true)
  const [error, setError] = React.useState<string | null>(null)

  React.useEffect(() => {
    fetchCargoListService()
      .then((result: API.CargoList.ResponseBody) => {
        setData(result)
        setLoading(false)
      })
      .catch((e: Error) => {
        setError(e.message)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Загрузка...</div>
  if (error) return <div>Не получилось загрузить данные. {error}</div>

  return <div>123</div>
}
