<?php

/* privileges/global_priv_table.twig */
class __TwigTemplate_6f007e4bf7c63ace7eedef9c847a0ab576c93cce44fdca033b449d0af5079f8a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        $context['_parent'] = $context;
        $context['_seq'] = twig_ensure_traversable((isset($context["priv_table"]) ? $context["priv_table"] : null));
        foreach ($context['_seq'] as $context["key"] => $context["table"]) {
            // line 2
            echo "    <fieldset>
        <legend>
            <input type=\"checkbox\" class=\"sub_checkall_box\" id=\"checkall_";
            // line 4
            echo twig_escape_filter($this->env, $this->getAttribute((isset($context["priv_table_names"]) ? $context["priv_table_names"] : null), $context["key"], array(), "array"), "html", null, true);
            echo "_priv\"
                title=\"";
            // line 5
            echo _gettext("Check all");
            echo "\" />
            <label for=\"checkall_";
            // line 6
            echo twig_escape_filter($this->env, $this->getAttribute((isset($context["priv_table_names"]) ? $context["priv_table_names"] : null), $context["key"], array(), "array"), "html", null, true);
            echo "_priv\">";
            echo twig_escape_filter($this->env, $this->getAttribute((isset($context["priv_table_names"]) ? $context["priv_table_names"] : null), $context["key"], array(), "array"), "html", null, true);
            echo "</label>
        </legend>
        ";
            // line 8
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable($context["table"]);
            foreach ($context['_seq'] as $context["_key"] => $context["priv"]) {
                // line 9
                echo "            ";
                $context["checked"] = ((($this->getAttribute((isset($context["row"]) ? $context["row"] : null), ($this->getAttribute($context["priv"], 0, array(), "array") . "_priv"), array(), "array", true, true) && ($this->getAttribute((isset($context["row"]) ? $context["row"] : null), ($this->getAttribute($context["priv"], 0, array(), "array") . "_priv"), array(), "array") == "Y"))) ? (" checked=\"checked\"") : (""));
                // line 10
                echo "            ";
                $context["formatted_priv"] = PhpMyAdmin\Server\Privileges::formatPrivilege($context["priv"], true);
                // line 11
                echo "            ";
                $this->loadTemplate("privileges/global_priv_tbl_item.twig", "privileges/global_priv_table.twig", 11)->display(array("checked" =>                 // line 12
(isset($context["checked"]) ? $context["checked"] : null), "formatted_priv" =>                 // line 13
(isset($context["formatted_priv"]) ? $context["formatted_priv"] : null), "priv" =>                 // line 14
$context["priv"]));
                // line 16
                echo "        ";
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_iterated'], $context['_key'], $context['priv'], $context['_parent'], $context['loop']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 17
            echo "    </fieldset>
";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['key'], $context['table'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
    }

    public function getTemplateName()
    {
        return "privileges/global_priv_table.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  64 => 17,  58 => 16,  56 => 14,  55 => 13,  54 => 12,  52 => 11,  49 => 10,  46 => 9,  42 => 8,  35 => 6,  31 => 5,  27 => 4,  23 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "privileges/global_priv_table.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/privileges/global_priv_table.twig");
    }
}
