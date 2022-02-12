import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/landingPages/HomeView.vue";
import CalendarView from "@/views/landingPages/CalendarView.vue"
import GroupsView from "@/views/landingPages/GroupsView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/termine",
      name: "Calendar",
      component: CalendarView,
    },
    {
      path: "/gruppen",
      name: "Groups",
      component: GroupsView,
    },
    {
      path: "/gruppen/:groupTechnicalName",
      name: "GroupPage",
      component: HomeView,
    },
    {
      path: "/was-ist-pfadfinder",
      name: "AboutScouting",
      component: HomeView,
    },
    {
      path: "/fotos",
      name: "Pictures",
      component: HomeView,
    },
    {
      path: "/downloads",
      name: "Downloads",
      component: HomeView,
    },
    {
      path: "/impressum",
      name: "Imprint",
      component: HomeView,
    },
    {
      path: "/faq",
      name: "FAQ",
      component: HomeView,
    },
    {
      path: "/datenschutz",
      name: "PrivacyPolicy",
      component: HomeView,
    },
  ],
});

export default router;
