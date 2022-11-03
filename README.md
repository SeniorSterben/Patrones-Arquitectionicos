# Patrones arquitectónicos de diseño de software
Son patrones de diseño que manejan los mecanismos de creación de objetos, cada patrón es utilizado conforme al uso que se necesite dar en diferentes situaciones.

En este repositorio vamos a explicar y a ejemplificar los patrones de creación de diseño de software más comunes.

# Singleton
Este patrón asegura que una clase tenga solo una instancia, también proporciona un punto de acceso global a esa misma instancia.
Entonces, en la clase puede haber como máximo una instancia.
# Factory
Define una interfaz para crear objetos, permite que las subclases decidan qué clases instanciar como se desee.
# Abstract Factory
Porporciona una interfaz para crear familias de objetos relacionados, sin especificar clases concretas. 
# Prototype
Este patrón especifica el tipo de objetos que se crearán utilizando una instancia prototípica. Los prototipos de nuevos productos generalmente se construyen antes de la producción completa, tambien puede ser un prototipo pasivo que no participe en la copia de si mismo.
# Facade
La fachada define una interfaz unificada de nivel superior para un subsistema que facilita su uso.
# Decorator
Este patrón adjunta dinámicamente responsabilidades adicionales a un objeto. Por ejemplo, las luces y adornos a un arbol de navidad.
# Proxy
Este patrón proporciona un sustituto o marcador de posición para brindar un acceso a un objeto, similar a un cheque el cual es representante de los fondos en una cuenta.
# Command
Este patrón permite encapsukar las solicitudes como objetos, lo que permite que los clientes se parametricen con figerentes solicitudes, es como anotar un objetivo encapsulándolo así para que otra persona cumpla con ese objetivo.
# Memento
Este patrón captura y externaliza el estado interno de un objeto para que luego el objeto pueda ser restaurado a ese estado, es decir que al desarmar 2 mecanismos iguales primero desarma uno y el otro se deja quieto como un backup para volver a armar el desarmado dejándolo como estaba al inicio.
# Observer
El observer se encarga de definir una relación de uno a muchos, cuan do un objeto cambia de estado, los demás son notificados y actualizados automáticamente.
# Strategy
Este patrón define un conjunto de algoritmos que se pueden usar indistintamente, el usuario decide cuál algoritmo le gustaría usar.
# Data Acces Object (DAO)
DAO nos permite separar la lógica de acceso de datos de los objetos, de tal forma que el patrón encapsula toda la lógica de acceso de datos al resto de la aplicación.
# Dependency Injection
Tiene como objetivo tomar la responsabilidad de crear las instancias de las clases que otro objeto necesita y suministrárselo para que esta clase los pueda utilizar.
# Model View Controller (MVC)
El modelo - vista - controlador comienza con una petición, esta llega al controlador el cual decide como usar los modelos, para recuperar los datos de una base de datos los cuales se agregan a una estructura de datos y esta pasa a una vista que muestra la página solicidada.
