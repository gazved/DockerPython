import sys
from api.client import AutomyClient
from services.filter_service import filter_races_by_date
from services.message_service import format_races_message, show_full_history

def main():
    try:
        client = AutomyClient()
        races_data = client.get_races("john.doe@gmail.com")
        past_races, upcoming_races = filter_races_by_date(races_data)
        
        print("\n" + "="*50, flush=True)
        print(format_races_message(upcoming_races, past_races), flush=True)
        
        while True:
            print("\nℹ️ Digite 'HISTORICO' para ver corridas passadas ou 'SAIR' para encerrar", flush=True)
            try:
                command = input(">>> ").strip().upper()
            except EOFError:
                print("\nModo não-interativo detectado. Encerrando...", flush=True)
                break
                
            if command == "HISTORICO":
                print(show_full_history(past_races), flush=True)
            elif command == "SAIR":
                print("\nObrigado por usar nosso sistema! 🏁", flush=True)
                break
            else:
                print("\n⚠️ Comando inválido. Tente novamente.", flush=True)
                
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}", file=sys.stderr, flush=True)
        sys.exit(1)

if __name__ == "__main__":
    main()