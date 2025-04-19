# Proyecto-de-Software

TIPO DE PROYECTO DE SOFTWARE: Interfaces de Programación de Aplicaciones (API)

TÍTULO: Despliegue de asistente virtual con Inteligencia Artificial Generativa en AWS

OBJETIVO PRINCIPAL:
- El proyecto tiene como finalidad crear un asistente virtual inteligente que apoye a la comunidad estudiantil de la Universidad Nacional de Ingeniería (UNI) respondiendo consultas relacionadas con trámites, reglamentos internos y autoridades universitarias. Este asistente será accesible a través de una interfaz conversacional amigable, desplegada sobre la infraestructura de nube de Amazon Web Services (AWS).

OBJETIVOS GENERALES: 
- Ayudar a la comunidad estudiantil ante cualquier consulta sobre reglamentos, trámites o información sobre autoridades de la Universidad Nacional de Ingeniería (UNI) del Perú
- Agilizar la burocracia interna de asesoría al estudiante
- Reducir la carga laboral de oficinas de la UNI 
- Automatizar los trámites estudiantiles de la UNI
- Permitir a las oficinas de la UNI dedicar más horas de trabajo a sus actividades específicas

METODOLOGÍAS A CONSIDERAR EN EL PROYECTO: 

- Desarrollo Incremental (para ir agregando funciones del chatbot por etapas).
- Metodología Ágil (por ejemplo, Scrum, con sprints semanales, ideal para prototipos y entregas frecuentes).
- Reutilización de componentes (al aprovechar APIs de OpenAI, frameworks de chatbot, servicios AWS preexistentes).

Entre estas 3 opciones nos basaremos princiálmente en la METODOLOGÍA INCREMENTAL al ser la mejor opción

Esta metodología es ideal para tu caso porque:

Te permite entregar funcionalidades útiles del asistente virtual en etapas progresivas durante las 8 semanas
Facilita obtener feedback temprano de los usuarios (estudiantes y personal administrativo) para hacer ajustes
Se alinea perfectamente con tu diagrama de arquitectura AWS, donde cada componente puede desarrollarse y conectarse incrementalmente
Reduce riesgos al detectar problemas en fases tempranas, especialmente en la integración con servicios de AWS y WhatsApp
Permite priorizar funcionalidades críticas primero (como consultas básicas) y luego agregar capacidades más sofisticadas

El enfoque incremental es superior a las otras opciones para este caso específico:

CASCADA sería demasiado rígida y no permitiría ajustes basados en feedback
POR COMPONENTES podría complicar la integración final de las piezas
PROGRAMACIÓN EXTREMA requeriría prácticas como programación en parejas que podrían no ser aplicables a tu contexto
