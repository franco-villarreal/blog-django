# BlogApp

Web simil blog desarrollada en Python con Django.

## Autor

Franco Villarreal - Desarrollo integral del proyecto

Originalmente, el grupo era de 3 integrantes pero 2 de ellos abandonaron la cursada poco tiempo antes de encarar el desarrollo del proyecto final.

## DEMO

// TODO: Add demo video url

## Casos de prueba

### 1. Sign In/Sign Up

1. Ir a http://localhost:8000/BlogApp/pages/ (al no estar con la sesión iniciada nos llevará al formulario de sign-in).
2. No tenemos usuario aun, pulsar en el enlace "Not registered? Sign up here", el cual no redirigirá al formulario de sign-up.
3. Ingresar los datos de prueba y pulsar el botón "Sign Up" (tras la creación exitosa seremos redirigidos al formulario de sign-in):
```json
{
    "username": "test"
    "password": "t1e2s3t4"
}
```
4. Ingresar nuestras credenciales según lo mencionado anteriormente y pulsar Sign In
5. Si ingresamos las credenciales correctas, seremos redirigidos a la Home page. En la parte superior derecha de la barra de navegación veremos nuestro nombre de usuario y la opción de cerrar la sesión.
6. Pulsar el botón "TEST SIGN OUT" para cerrar la sesión.
7. Seremos redirigidos a la pantalla de cierre de sesión y se nos dará la opción de ir nuevamente al sign-in.

### 2. Posts

1. Ir a la Home page o bien http://localhost:8000/BlogApp/pages/
2. Allí veremos un formulario para filtrar las publicaciones por nombre de usuario y por debajo la lista de publicaciones existentes, si las hubiere. En este caso, deberíamos ver el mensaje "Ops! Seems like there are not posts now."
3. Pulsar el botón "New" para acceder al formulario de creación de publicaciones.
4. Ingresar los datos de prueba y pulsar el botón "New" para crear una nueva publicación:
```json
{
    "title": "Lorem ipsum",
    "subtitle": "Lorem ipsum dolor",
    "article": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque venenatis sit amet felis nec tincidunt. Donec porttitor eros nisi, id vestibulum eros luctus mattis. Curabitur pellentesque consequat felis, et tristique magna malesuada sit amet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur volutpat arcu quis sapien lacinia, in venenatis eros semper. Aliquam dapibus sapien id neque volutpat, a tincidunt lorem vestibulum. Aenean eu sapien et risus tempus dapibus. Pellentesque hendrerit purus erat, in molestie arcu ultrices scelerisque. Aenean nec nunc eu nunc vulputate scelerisque. Phasellus molestie urna ac facilisis luctus. Nullam aliquet lectus ante, eget dictum orci lobortis a. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vitae rhoncus eros. Ut tincidunt, mi non rutrum auctor, justo odio tempus leo, sit amet dignissim augue diam a lacus."
}
```
5. Posteriormente veremos el detalle de la publicación creada. Automáticamente se registrarán los datos del usuario, la fecha de creación y tendremos la posibilidad de editar o eliminar la publicación (si solo si el usuario autenticado coincide con el autor).
6. Pulsar el botón "Edit" para acceder al formulario de edición e ingresar los datos:
```json
{
    "title": "Edited post",
    "subtitle": "Lorem ipsum dolor",
    "article": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque venenatis sit amet felis nec tincidunt. Donec porttitor eros nisi, id vestibulum eros luctus mattis. Curabitur pellentesque consequat felis, et tristique magna malesuada sit amet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur volutpat arcu quis sapien lacinia, in venenatis eros semper. Aliquam dapibus sapien id neque volutpat, a tincidunt lorem vestibulum. Aenean eu sapien et risus tempus dapibus. Pellentesque hendrerit purus erat, in molestie arcu ultrices scelerisque. Aenean nec nunc eu nunc vulputate scelerisque. Phasellus molestie urna ac facilisis luctus. Nullam aliquet lectus ante, eget dictum orci lobortis a. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vitae rhoncus eros. Ut tincidunt, mi non rutrum auctor, justo odio tempus leo, sit amet dignissim augue diam a lacus."
}
```
7. Pulsar el botón "Edit" para guardar los cambios. Seremos redirigidos a la vista de detalles de la publicación.
8. Pulsar ahora el botón "Delete" para eliminar la publicación. Luego seremos redirigidos a la Home page nuevamente.

### 3. Post Comments

1. Crear una nueva publicación tal y como se explicó en el caso de prueba 2.
2. Desde la Home page, ingresar al detalle de la publicación creada.
3. Al final del artículo, veremos la lista de comentarios de usuarios. Cualquier usuario autenticado puede dejar comentarios en las publicaciones y solo el autor de dicho comentario tiene la capacidad de borrarlo.
4. Ingresar un mensaje en el campo "Message" y pulsar el botón "Send".
5. Automáticamente se recargará la página, se sumará 1 comentario a la lista y veremos el mensaje que acabados de guardar con los datos del usuario y la fecha de creación.
6. Al ser los autores del comentario, tendremos a nuestra disposición un botón "Remove comment" para eliminarlo.
7. Pulsar "Remove comment".
8. La página se recargará y ya no veremos el comentario.