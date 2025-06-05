import { Link } from "react-router-dom"
import { cn } from "@/lib/utils"

export function MainNav({
  className,
  ...props
}: React.HTMLAttributes<HTMLElement>) {
  return (
    <nav
      className={cn("flex items-center space-x-4 lg:space-x-6", className)}
      {...props}
    >
      <Link
        to="/efko"
        className="text-sm font-medium transition-colors hover:text-primary"
      >
        Efko
      </Link>
      <Link
        to="/trucker"
        className="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
      >
        Trucker
      </Link>
      <Link
        to="/efes"
        className="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
      >
        Efes
      </Link>
      <Link
        to="/Ascona"
        className="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
      >
        Ascona
      </Link>
    </nav>
  )
}
