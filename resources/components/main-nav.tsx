import { Link, useLocation } from "react-router-dom"
import { cn } from "@/lib/utils"

export function MainNav({
  className,
  ...props
}: React.HTMLAttributes<HTMLElement>) {
  const location = useLocation()

  const links = [
    { to: "/efko", label: "Efko" },
    { to: "/trucker", label: "Trucker" },
    { to: "/efes", label: "Efes" },
    { to: "/ascona", label: "Ascona" },
  ]

  return (
    <div className="fixed inset-x-0 bottom-0 z-50">
      <div className="flex h-16 items-center justify-center space-x-8 px-4">
        <nav
          className={cn("flex items-center space-x-8", className)}
          {...props}
        >
          {links.map(({ to, label }) => {
            const isActive = location.pathname === to
            return (
              <Link
                key={to}
                to={to}
                className={cn(
                  "relative px-3 py-2 text-sm font-medium transition-colors",
                  // цвет текста и подчеркивания для активного/неактивного состояния
                  isActive
                    ? "text-primary after:bg-primary"
                    : "text-primary-foreground after:bg-primary-foreground",
                  // общие стили для псевдо-элемента :after
                  "after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:h-0.5 after:w-6 after:rounded-full",
                  // hover-эффект для подчеркивания
                  "hover:after:bg-primary"
                )}
              >
                {label}
              </Link>
            )
          })}
        </nav>
      </div>
    </div>
  )
}
