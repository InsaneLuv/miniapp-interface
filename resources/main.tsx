import "vite/modulepreload-polyfill"

import React from "react"
import ReactDOM from "react-dom/client"
import App from "@/App.tsx"
import "@/main.css"
import { BrowserRouter } from "react-router-dom"
import AuthProvider from "@/contexts/AuthProvider.tsx"
import { Toaster } from "@/components/ui/sonner"

import { postEvent } from "@telegram-apps/sdk"

postEvent("web_app_expand")
postEvent("web_app_setup_main_button", { is_visible: false })
postEvent("web_app_setup_swipe_behavior", { allow_vertical_swipe: false })
postEvent("web_app_ready")

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />

        <Toaster />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
)
