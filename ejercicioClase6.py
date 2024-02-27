class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso

    def calcular_salario(self):
        pass


class EmpleadoAComision(Empleado):
    SALARIO_MINIMO_DEFAULT = 200000
    MONTO_POR_CLIENTE_DEFAULT = 15000

    def __init__(
        self, dni, nombre, apellido, anioIngreso, clientes_captados=None,
        monto_por_cliente=None
    ):
        super().__init__(dni, nombre, apellido, anioIngreso)
        self.clientes_captados = (
            clientes_captados if clientes_captados is not None else 0
        )
        self.monto_por_cliente = (
            monto_por_cliente if monto_por_cliente is not None else
            self.MONTO_POR_CLIENTE_DEFAULT
        )

    def calcular_salario(self):
        salario_base = self.SALARIO_MINIMO_DEFAULT
        adicional = self.clientes_captados * self.monto_por_cliente
        salario_total = salario_base + adicional
        return salario_total

    def mostrar_adicional(self):
        return self.clientes_captados * self.monto_por_cliente


class EmpleadoConSalarioFijo(Empleado):
    SUELDO_BASICO = 250000

    def __init__(self, dni, nombre, apellido, anioIngreso):
        super().__init__(dni, nombre, apellido, anioIngreso)
        self.anioIngreso = anioIngreso

    def calcular_salario(self):
        antiguedad = 2024 - self.anioIngreso
        if antiguedad < 2:
            return self.SUELDO_BASICO
        elif 2 <= antiguedad <= 5:
            return self.SUELDO_BASICO * 1.05
        else:
            return self.SUELDO_BASICO * 1.1


empleados = [
    EmpleadoAComision(31254236, "Guido", "Lopez", 2018, clientes_captados=8),
    EmpleadoAComision(19541285, "Carlos", "Garcia", 2019, clientes_captados=6),
    EmpleadoAComision(92707377, "Rosa", "Diaz", 2021, clientes_captados=9),
    EmpleadoAComision(32542872, "MOnica", "Mendez", 2019, clientes_captados=5),
    EmpleadoAComision(33568423, "Majo", "Rios", 2021, clientes_captados=0),
    EmpleadoAComision(24445254, "Ailin", "Silva", 2018, clientes_captados=7),
    EmpleadoConSalarioFijo(32547215, "Joaquin", "Soto", 2017),
    EmpleadoConSalarioFijo(30254266, "Ana", "Vidal", 2016),
    EmpleadoConSalarioFijo(25478125, "Sofia", "Vergara", 2015),
    EmpleadoConSalarioFijo(38510005, "Diego", "Torres", 2023),
]


def mostrar_salarios(empleados):
    for empleado in empleados:
        salario = empleado.calcular_salario()
        tipo_empleado = "Empleado A Comision" if isinstance(
            empleado, EmpleadoAComision) else "Empleado con Salario Fijo"
        antiguedad = 2024 - empleado.anioIngreso if hasattr(
            empleado, 'anioIngreso') else 0
        clientes_captados = empleado.clientes_captados if hasattr(
            empleado, 'clientes_captados') else 0

        print(f"{empleado.nombre} {empleado.apellido}:")
        print(f"Tipo de Empleado: {tipo_empleado}")
        print(f"Anios de Antiguedad: {antiguedad}")
        if isinstance(empleado, EmpleadoAComision):
            print(f"Clientes Captados: {clientes_captados}")

        print(f"Salario: ${salario:.2f}")
        if isinstance(empleado, EmpleadoAComision):
            adicional = empleado.mostrar_adicional()
            if clientes_captados > 0:
                print(f"Debido a {clientes_captados} clientes"
                      f" captados este mes,gano un adicional "
                      f"de ${adicional:.2f}")
            else:
                print("Este mes gano el salario mínimo, no capto clientes.")
        print("-" * 40)


mostrar_salarios(empleados)


def empleadoConMasClientes(empleados):
    empleado_max_clientes = None
    max_clientes = -1

    for empleado in empleados:
        if isinstance(empleado, EmpleadoAComision):
            clientes_captados = empleado.clientes_captados
            if clientes_captados > max_clientes:
                max_clientes = clientes_captados
                empleado_max_clientes = empleado

    return empleado_max_clientes


empleado_max_clientes = empleadoConMasClientes(empleados)

if empleado_max_clientes is not None:
    print(f"Empleado con más clientes captados: "
          f"{empleado_max_clientes.nombre} {empleado_max_clientes.apellido}")
    print(f"Cantidad de clientes captados:"
          f" {empleado_max_clientes.clientes_captados}")
else:
    print("No hay empleados con clientes captados.")

while True:
    print("\nMenú Principal:")
    print("1. Ver salarios")
    print("2. Ver Empleado del Mes")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        mostrar_salarios(empleados)
    elif opcion == "2":
        empleado_mes = empleado_max_clientes(empleados)
        if empleado_mes is not None:
            print(f"Empleado del Mes: "
                  f" {empleado_mes.nombre} {empleado_mes.apellido}")
            print(f"Cantidad de clientes captados: "
                  f"{empleado_max_clientes.clientes_captados}")
        else:
            print("No hay Empleado del Mes.")
    elif opcion == "3":
        print("Saliendo de la aplicación. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
