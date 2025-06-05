import { useAuth } from "@/contexts/AuthProvider";
import MainLayout from "@/layouts/MainLayout";
import { useEffect } from "react";
import { MainNav } from "@/components/main-nav";
import { CargoShortTable } from "@/components/ui/test";

const Home: React.FC = () => {
    const { auth } = useAuth();

    // useEffect(() => {
    //     // Этот useEffect в данный момент пуст.
    //     // Если здесь предполагается какая-то логика, связанная с auth.token,
    //     // ее следует добавить. В противном случае, его можно удалить, если он не нужен.
    // }, [auth?.token]);

    return (
        <MainLayout
            title="Торги"
            description="Страница торгов"
            keywords="home"
        >


            <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
                <div className="flex-1 space-y-4 p-8 pt-6">
                    <CargoShortTable />
                </div>
            </div>

            <div className="fixed inset-x-0 bottom-0 z-50 border-t bg-background">
                <div className="flex h-16 items-center justify-center space-x-4 px-4">
                    <MainNav />
                </div>
            </div>
        </MainLayout>
    );
};

export default Home;