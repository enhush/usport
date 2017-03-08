<template lang="html">
  <aside class="menu">
    <div class="card">
      <div class="card-image has-text-centered">
        <i class="fa fa-area-chart"></i>
      </div>
      <div class="card-content">
        МУҮХ-ны бүртгэлийн систем
      </div>
    </div>
    <ul class="menu-list">
      <li>
        <router-link
          :to="{name: 'club'}"
          :class="{'is-active': $route.matched.some(
            record => record.name == 'club' ||
                      record.name == 'club-add'
            )}">
            
          Клуб
        </router-link>
      </li>
      <li>
        <a>Шүүгчид</a>
        <ul v-show="false">
          <li><a>-Бүртгэл</a></li>
          <li><a>-Хүсэлт</a></li>
        </ul>
      </li>
      <li><a>Тамирчид</a></li>
    </ul>
    <p class="menu-label">
      <hr class="is-marginless">
    </p>
    <ul class="menu-list">
      <li><a>Тэмцээн</a></li>
      <li><a>Авиралт</a></li>
      <li><a>Авиралтын зам</a></li>
      <li><a>Арга хэмжээ</a></li>
    </ul>
    <p class="menu-label">
      <hr class="is-marginless">
    </p>
    <ul class="menu-list">
      <li><a>Спортын төрөл</a></li>
      <li><a>Авиралтын замын зэрэглэл</a></li>
    </ul>
    <p class="menu-label">
      <hr class="is-marginless">
    </p>
    <ul class="menu-list">
      <li><a>Нууц үг солих</a></li>
      <li><a>Гарах</a></li>
    </ul>
  </aside>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
.card {
  padding: 10px 0;
  box-shadow: none;
  background-color: #FAFAFA;
}
</style>
