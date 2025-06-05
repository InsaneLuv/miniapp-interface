import axios from "axios"
import { API } from "@/types/api"

const APP_URL = import.meta.env.APP_URL || ""

export const fetchCargoListService = async () => {
    try {
        const response = await axios.get<API.CargoList.ResponseBody>(
            `${APP_URL}/api/orders`
        )
        return response.data
    } catch (error) {
        throw error
    }
}
