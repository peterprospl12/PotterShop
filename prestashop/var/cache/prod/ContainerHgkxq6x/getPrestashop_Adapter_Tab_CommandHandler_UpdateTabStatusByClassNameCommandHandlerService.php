<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.adapter.tab.command_handler.update_tab_status_by_class_name_command_handler' shared service.

return $this->services['prestashop.adapter.tab.command_handler.update_tab_status_by_class_name_command_handler'] = new \PrestaShop\PrestaShop\Adapter\Tab\CommandHandler\UpdateTabStatusByClassNameHandler(${($_ = isset($this->services['doctrine.orm.default_entity_manager']) ? $this->services['doctrine.orm.default_entity_manager'] : $this->getDoctrine_Orm_DefaultEntityManagerService()) && false ?: '_'});
