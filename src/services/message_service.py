def format_races_message(upcoming_races, past_races):
    messages = ["🏎️ BEM-VINDO AO KARTÓDROMO DIGITAL!"]
    
    if upcoming_races:
        messages.append("\n🚀 PRÓXIMAS CORRIDAS:")
        for race in sorted(upcoming_races, key=lambda x: x['data_agendamento']):
            messages.append(
                f"- {race['data_agendamento']} às {race['horario_agendamento']} "
                f"({race['qtde_pessoas']} pessoas)"
            )
    
    if past_races:
        messages.append("\n⏳ CORRIDAS PASSADAS (digite 'HISTORICO' para ver):")
        messages.append(f"Total: {len(past_races)} corridas realizadas")
    
    return "\n".join(messages)

def show_full_history(past_races):
    messages = ["\n📜 HISTÓRICO COMPLETO DE CORRIDAS:"]
    for idx, race in enumerate(sorted(past_races, key=lambda x: x['data_agendamento']), 1):
        messages.append(
            f"{idx}. {race['data_agendamento']} às {race['horario_agendamento']} - "
            f"{race['qtde_pessoas']} pessoas | Agendado em: {race['datetime_formulario']}"
        )
    return "\n".join(messages)