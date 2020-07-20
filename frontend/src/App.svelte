<script>
  import { onMount, setContext } from "svelte";
  import {
    key as userContextKey,
    initialValue as userContextInitialValue
  } from "./userContext";
  import Registration from "./Registration.svelte";
  onMount(() => {
    setContext(userContextKey, userContextInitialValue);
  });
  const submit = ({ email, password }) =>
    new Promise((resolve, reject) => {
      setTimeout(() => {
        setContext(userContextKey, {
          name: "Foo",
          lastName: "Bar",
          email: "foo@bar.com"
        });
        resolve();
      }, 1000);
    });
</script>

<section>
  <Registration {submit} />
</section>