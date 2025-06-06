import { Route, Routes, useLocation, useNavigate } from "react-router-dom"
import EfkoPage from "@/pages/clients/Efko"
import PageNotFound from "@/pages/PageNotFound"
import { ThemeProvider } from "@/components/theme-provider"
import TruckerPage from "./pages/clients/Trucker"
import { MainNav } from "./components/main-nav"

const App: React.FC = () => {
  return (
    <ThemeProvider defaultTheme="system" storageKey="dma-ui-theme">
      <Routes>
        <Route path="/" element={<EfkoPage />} />
        <Route path="/Efko" element={<EfkoPage />} />
        <Route path="/Trucker" element={<TruckerPage />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>

      <MainNav />
    </ThemeProvider>
  )
}

export default App
